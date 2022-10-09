from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# options for how many guests in the booking
GUESTS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
)

# options for the time of the booking
TIME = (
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
)


class Booking(models.Model):
    """Model that is used to store the data that the user enters in the
    booking form. The User Foreignkey associates each booking
    with a particular user.
    """
    class Meta:
        unique_together = ('date', 'time', 'guests')

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_booking")
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.IntegerField(blank=True, null=True)
    guests = models.CharField(max_length=2, choices=GUESTS, default='4')
    time = models.CharField(max_length=30, choices=TIME, default='19:00')
    date = models.DateField()

    def __str__(self):
        return self.name
