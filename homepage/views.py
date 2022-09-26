from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def menu_page(request):
    return render(request, 'menu_page.html')