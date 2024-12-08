from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")
def theory(request):
    return render(request, "main/theory.html")
def chords(request):
    return render(request, "main/chords.html")
def pentatonix(request):
    return render(request, "main/pentatonix.html")