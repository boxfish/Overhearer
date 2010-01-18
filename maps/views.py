from django.conf import settings 
from django.http import HttpResponse, HttpResponseNotFound

import os
import math
import yaml
import mapnik

try:
    # 2.6 will have a json module in the stdlib
    import json
except ImportError:
    try:
        # simplejson is the thing from which json was derived anyway...
        import simplejson as json
    except ImportError:
        print "No suitable json library found"


#load the config file
f = open(os.path.join(os.path.dirname(__file__), 'config.yaml'))
CONFIG = yaml.load(f)
f.close()
# read the config file to speed up tile generation
max_zoom = int(CONFIG.get("tiles").get("max_zoom"))
size = int(CONFIG.get("tiles").get("size"))
buffer_size = int(CONFIG.get("tiles").get("size"))
caching_map = int(CONFIG.get("tiles").get("caching_map"))
caching_image = CONFIG.get("tiles").get("caching_image")
cached_maps = {}
        
MERC_PROJ4 = "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs +over"
mercator = mapnik.Projection(MERC_PROJ4)

class SphericalMercator(object):
    """
    Python class defining Spherical Mercator Projection.
    
    Originally from:  
      http://svn.openstreetmap.org/applications/rendering/mapnik/generate_tiles.py
    """
    def __init__(self,levels=18,size=256):
        self.Bc = []
        self.Cc = []
        self.zc = []
        self.Ac = []
        self.DEG_TO_RAD = math.pi/180
        self.RAD_TO_DEG = 180/math.pi
        self.cache = {}
        self.size = size
        for d in range(0,levels):
            e = size/2.0;
            self.Bc.append(size/360.0)
            self.Cc.append(size/(2.0 * math.pi))
            self.zc.append((e,e))
            self.Ac.append(size)
            size *= 2.0

    @classmethod
    def minmax(a,b,c):
        a = max(a,b)
        a = min(a,c)
        return a

    def ll_to_px(self,px,zoom):
        d = self.zc[zoom]
        e = round(d[0] + px[0] * self.Bc[zoom])
        f = self.minmax(math.sin(DEG_TO_RAD * px[1]),-0.9999,0.9999)
        g = round(d[1] + 0.5 * math.log((1+f)/(1-f))*-self.Cc[zoom])
        return (e,g)
    
    def px_to_ll(self,px,zoom):
        """ Convert pixel postion to LatLong (EPSG:4326) """
        e = self.zc[zoom]
        f = (px[0] - e[0])/self.Bc[zoom]
        g = (px[1] - e[1])/-self.Cc[zoom]
        h = self.RAD_TO_DEG * ( 2 * math.atan(math.exp(g)) - 0.5 * math.pi)
        return (f,h)
    
    def xyz_to_envelope(self,x,y,zoom):
        """ Convert XYZ to mapnik.Envelope """
        #e_id = '%s-%s-%s' % (x,y,zoom)
        #if e_id in self.cache:
        #    return self.cache[e_id]
        ll = (x * self.size,(y + 1) * self.size)
        ur = ((x + 1) * self.size, y * self.size)
        minx,miny = self.px_to_ll(ll,zoom)
        maxx,maxy = self.px_to_ll(ur,zoom)
        lonlat_bbox = mapnik.Envelope(minx,miny,maxx,maxy)
        env = mercator.forward(lonlat_bbox)
        #self.cache[e_id] = env
        return env

merc = SphericalMercator(levels=max_zoom,size=size)

def map_static(request, mapfile_path, format):
    img_file = os.path.join(os.path.dirname(__file__), CONFIG.get("mapfile_dir"), mapfile_path, "map.%s" % format)
    img = None
    if request.method == "GET":
        if os.path.exists(img_file):
            img = mapnik.Image.open(str(img_file))
    elif request.method == "POST":
        data = json.loads(request.raw_post_data)
        mapnik_map_file = os.path.join(os.path.dirname(__file__), CONFIG.get("mapfile_dir"), mapfile_path, "map.xml")
        # laod the width and height of the image
        width = int(data.get("width", CONFIG.get("static").get("width")))
        height = int(data.get("height", CONFIG.get("static").get("height")))
        print width
        m = mapnik.Map(width, height)
        mapnik.load_map(m, str(mapnik_map_file))
        print "TEST"
        # load the bbox
        minx = float(data.get("minx", "-180.0"))
        miny = float(data.get("miny", "-90.0"))
        maxx = float(data.get("maxx", "180.0"))
        maxy = float(data.get("maxy", "90.0"))
        env = mapnik.Envelope(minx, miny, maxx, maxy)
        #env = mercator.forward(lonlat_bbox)
        
        m.zoom_to_box(env)
        img = mapnik.Image(width, height)
        mapnik.render(m, img)
        img.save(str(img_file), str(format))
    if img:
        response = img.tostring(str(format))
        mime_type = 'image/%s' % format
        return HttpResponse(response, mimetype=mime_type)
    else:
        return HttpResponseNotFound("The image cannot be found!")        
    
def map_tiles(request, mapfile_path, zoom, x, y, format):
    if request.method == "GET":
        m = None
        img = None
        if caching_image:
            tile_file = os.path.join(os.path.dirname(__file__), CONFIG.get("mapfile_dir"), mapfile_path, zoom, x,'%s.%s' % (y, format))
            if os.path.exists(tile_file):
                img = mapnik.Image.open(str(tile_file))
        if not img:
            if caching_map > 0:
                cached_map = cached_maps.get("mapfile_path", None)
                if cached_map:
                    m = cached_map
                if len(cached_maps) >= caching_map:
                    cached_maps.clear()
            if not m:
                mapnik_map_file = os.path.join(os.path.dirname(__file__), CONFIG.get("mapfile_dir"), mapfile_path, "map.xml")
                m = mapnik.Map(size, size)
                mapnik.load_map(m, str(mapnik_map_file))
                if caching_map > 0:
                    cached_maps[mapfile_path] = m
            envelope = merc.xyz_to_envelope(int(x),int(y),int(zoom))
            m.zoom_to_box(envelope)
            m.buffer_size = buffer_size
            img = mapnik.Image(size, size)
            mapnik.render(m,img)
            if caching_image:
                tile_file = os.path.join(os.path.dirname(__file__), CONFIG.get("mapfile_dir"), mapfile_path, zoom, x,'%s.%s' % (y, format))
                dirname = os.path.dirname(tile_file)
                if not os.path.exists(dirname):
                    os.makedirs(dirname)
                img.save(str(tile_file), str(format))
        response = img.tostring(str(format))
        mime_type = 'image/%s' % format
        return HttpResponse(response, mimetype=mime_type)