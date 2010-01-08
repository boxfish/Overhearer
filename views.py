from django.conf import settings 
from django.http import HttpResponse

def indexHandler(request):
    return HttpResponse("Hello, world. You're at the index.")


