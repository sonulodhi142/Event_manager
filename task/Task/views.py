from django.shortcuts import HttpResponse

def Home(req):
    return HttpResponse("This is my home view ")