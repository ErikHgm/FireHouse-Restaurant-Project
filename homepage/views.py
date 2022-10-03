from django.shortcuts import render, redirect, get_object_or_404
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


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('mybookings_page')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('mybookings_page')