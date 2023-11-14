from django.forms import ModelForm
from .models import booking_Model


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = booking_Model
        fields = "__all__"
