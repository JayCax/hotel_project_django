from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError

from .models import Room

class BookingForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'booking_start': DateInput(attrs={"type": "date"}),
            'booking_duration': TextInput(attrs={"type": "number", "min": "1"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Meetings cannot be in the past")
        return d