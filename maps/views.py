from django.conf import settings 
from django.http import HttpResponse

import os
import yaml

def test(request):
    return HttpResponse("Hello, world. test map.")