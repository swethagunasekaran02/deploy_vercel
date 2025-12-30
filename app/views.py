from django.shortcuts import render

def home(request):
    return render(request, 'app/index.html')

# Create your views here.
