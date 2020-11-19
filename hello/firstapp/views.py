from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def resume(request):
    return render(request, "resume.html")

def resumeEngl(request):
    return render(request, "resumeEngl.html")