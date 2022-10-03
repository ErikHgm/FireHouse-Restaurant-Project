from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm


def home(request):
    return render(request, 'index.html')


def menu_page(request):
    return render(request, 'menu_page.html')


def booking_page(request):
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            return redirect('mybookings_page')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'booking.html', context)


def mybookings_page(request):
    bookings = Booking.objects.all()

    context = {
       'bookings': bookings
        }
    return render(request, 'mybookings.html', context)