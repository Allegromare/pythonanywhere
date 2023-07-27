from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse


# def index(request):
#    return HttpResponse("WEBSITE")


def index(request):
    return render(request, "website/index.html")
