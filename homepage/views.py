from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def menu_page(request):
    return render(request, 'menu_page.html')


def booking_page(request):
    return render(request, 'booking.html')
