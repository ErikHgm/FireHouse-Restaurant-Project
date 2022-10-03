from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """
    This class provides a widget that the user can
    click on. It cretes a better UX when choosing the date
    for the booking.
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """
    This class generates a form based on the fields in the
    Booking model, except for the User field.
    It will then be displayed in the Booking template
    in order for the user to make their booking using the form.
    """
    class Meta:
        model = Booking
        exclude = ('user', )
        widgets = {
            'date': DateInput(),
        }
