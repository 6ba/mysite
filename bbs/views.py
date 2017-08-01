from django.shortcuts import render

# Create your views here.

def index(request):
    print(request.META["USERNAME"])
    return render(request, "bbs/index.html")

