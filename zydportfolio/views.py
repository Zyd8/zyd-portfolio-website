from django.shortcuts import render

def about(request):
    return render(request, "about.html")

def resume(request):
    return render(request, "resume.html")
