$(document).ready(function () {
	/**********************************
	// PlanGraph Initialization
	***********************************/
	var pgSettings = {
		iRootOrientation: "top", 
		linkType: "B",
		nodeWidth : 120,
		nodeHeight : 20,
		treeWidth : 450,
		treeHeight : 450
	};
	
	var pgStyles = {
		blanket : {stroke: "none", fill: "#fff", "opacity": 0.0},
		link : {
			stroke:"#333333",
			"stroke-width" : 2
		},
		action : {
			init : {
				box : {stroke: "#003DF5", "stroke-dasharray": "-.", fill: "#fff", "fill-opacity": 0.8, "stroke-width": 2},
				label : {fill:"#000", "font-size": 10}
			},
			inProgress : {
				box : {fill: "#0F4BFF", stroke: "#003DF5", "fill-opacity": 0.8, "stroke-width": 2},
				label : {fill:"#fff", "font-size": 10}
			},
			success : {
				box : {fill: "#FFF", stroke: "#003DF5", "fill-opacity": 0.8, "stroke-width": 2},
				label : {fill:"#000", "font-size": 10}				
			},
			failure : {
				box : {fill: "#FF794D", stroke: "#003DF5", "fill-opacity": 0.8, "stroke-width": 2},
				label : {fill:"#fff", "font-size": 10}
			}
		},
		parameter : {
			notReady : {
				box : {fill: "#fff", stroke: "#FF6633", "stroke-dasharray": "-.", "fill-opacity": 0.8, "stroke-width": 2},
				label : {fill:"#000", "font-size": 10}
			},
			hasValue : {
				box : {fill: "#FF794D", stroke: "#FF6633", "fill-opacity": 0.8, "stroke-width": 2},
				label : {fill:"#fff", "font-size": 10}
			},
			success : {
				box : {fill: "#fff", stroke: "#FF6633", "fill-opacity": 0.8, "stroke-width": 2},
				label : {fill:"#000", "font-size": 10}
			},
			failure : {
				box : {fill: "#FF794D", stroke: "#FF6633", "fill-opacity": 0.8, "stroke-width": 2},
				label : {fill:"#fff", "font-size": 10}
			}
		},
		tooltip : {
			frame : {fill: "#303030", stroke: "#474747", "stroke-width": 2, "fill-opacity": 0.8},
			label : {fill:"#fff", "font-size": 9},
			mentalState : {
				empty : {"fill-opacity": 1, stroke : '#838383', "stroke-width": 1},
				fill : {fill: '#00B88A', "fill-opacity": 0.8, stroke : '#838383', "stroke-width": 1}
			}
		},
		boxMouseOver : {
			"fill-opacity" : 0.9,
			"stroke-width": 4
		},
		labelMouseOver : {
			
		},
		boxMouseOut : {
			"fill-opacity" : 0.8,
			"stroke-width": 2
		},
		labelMouseOut : {
			
		}	
	};
	
	var pg = new PlanGraph('pgTabs-vis', pgSettings, pgStyles);
	
	/**********************************
	// Map Initialization
	***********************************/
	var mapSettings = {
		//projection: new OpenLayers.Projection('EPSG:900913'),
		//displayProjection: new OpenLayers.Projection('EPSG:900913'),
		//units: 'm',
		//numZoomLevels: 20,
		//maxResolution: '156543.0339',
		//maxExtent: OpenLayers.Bounds.fromString('-8679157,4971158.57086,-8655805.51884,4993707.49420')
		maxExtent: new OpenLayers.Bounds(-130, 14, -60, 55)
	};
	var map = new OpenLayers.Map('mapTabs-map', mapSettings);
	var wmcParser = new OpenLayers.Format.WMC({'layerOptions': {buffer: 0}, 'version':'1.1.0.ex'});
	var addControls = function() {
		//map.addControl(new OpenLayers.Control.PanZoom());
		map.addControl(new OpenLayers.Control.LayerSwitcher());
		//map.addControl(new OpenLayers.Control.MousePosition());
		map.addControl(new OpenLayers.Control.PanZoomBar());
		map.addControl(new OpenLayers.Control.ScaleLine());
		map.addControl(new OpenLayers.Control.Attribution());
	};
	var displayMapViz = function(xmlText) {
		map.destroy();
		map = wmcParser.read(xmlText, {map: 'mapTabs-map'});
		//map.events.register('moveend', map, mapMoveEnd);
		addControls();
	}
	/**********************************
	// UI Initialization
	***********************************/
	var pgTabs = $('#pgTabs').tabs();
	var mapTabs = $('#mapTabs').tabs();
	
	var pgEditor = new CodeMirror(CodeMirror.replace('pgXML-placeholder'), {
		parserfile: 'parsexml.js',
		path: "static/lib/codemirror/js/",
		stylesheet: "static/lib/codemirror/css/xmlcolors.css",
		height: '430px',
		indentUnit: 2,
		iframeClass: 'xmleditor',
		reindentOnLoad: true
	});
	
	var mapEditor = new CodeMirror(CodeMirror.replace('mapXML-placeholder'), {
		parserfile: 'parsexml.js',
		path: "static/lib/codemirror/js/",
		stylesheet: "static/lib/codemirror/css/xmlcolors.css",
		height: '430px',
		indentUnit: 2,
		iframeClass: 'xmleditor',
		reindentOnLoad: true
	});	
	
	var onSendMessageSuccess = function(response, textStatus) {
		//response = JSON.parse(response);
		response = $.evalJSON(response);
		if (response.status === "success") {
			requestPlanGraph();
			requestMap();
		}
	};
	
	var sendCurrentMessage = function() {
		var url = baseUrl + "dialogues/" + currDialogueId + "/messages/";
		var requestData = {"speakerId" : currSpeakerId, "message" : currMessage};
		$.post(url, $.toJSON(requestData), onSendMessageSuccess);
	};
	
	var onRequestPlanGraphSuccess = function(response) {
		//IE
		if (window.ActiveXObject){
			var xmlString = response.xml;
		}
		else{
			var xmlString = (new XMLSerializer()).serializeToString(response);
		}
		pgEditor.setCode(xmlString);
		pg.clear();
		pg.loadXML(response);
		pg.draw();
	};
	
	var requestPlanGraph = function() {
		var url = baseUrl + "dialogues/" + currDialogueId + "/plangraph/";
		$.ajax({
			type: "GET",
			url: url,
			dataType: "xml",
			success: onRequestPlanGraphSuccess
		});
	};
	
	var onRequestMapSuccess = function(response) {
		mapEditor.setCode(response);
		displayMapViz(response);
	};
	
	var requestMap = function() {
		var url = baseUrl + "dialogues/" + currDialogueId + "/map/";
		$.ajax({
			type: "GET",
			url: url,
			dataType: "text",
			success: onRequestMapSuccess
		});
	};
	
	$('#chatSubmit').click(function() {
		currSpeakerId = $('#speakerId').val();
		currMessage = $('#message').val();
		if (currSpeakerId && currMessage) {
			html = '<li class="ui-widget-content">' + currSpeakerId + ': ' + currMessage +'</li>';
			$('#chatList').append(html);
			sendCurrentMessage();
			$('option:selected', 'select').removeAttr('selected').next('option').attr('selected', 'selected');
			$('#message').val('');
		}
	});
	
	// initiate the dialogue
	var baseUrl = "http://127.0.0.1:8080/"
	var url = baseUrl + "dialogues/"
	var currDialogueId = "";
	var currSpeakerId = "";
	var currMessage = "";
	
  	var requestData = {id : "test123",participants : [{name: "Jim",id:"jim@abc.com"}, {name: "Jill",id:"jill@abc.com"}]};
  	$.post(url, $.toJSON(requestData), function(response, textStatus) {
		//response = JSON.parse(response);
		response = $.evalJSON(response)
		if (response.status === "success") {
			currDialogueId = response.dialogue.id;
		}
	});
	
	
});