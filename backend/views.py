from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "backend/index.html")

def banner(request):
    return render(request, "backend/banner.html")