from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'reservation_date', 'reservation_slot']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'id': 'first_name',
                    'class': 'form-control',
                    'placeholder': 'First name',
                }
            ),
            'reservation_date': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'id': 'reservation_date',
                    'class': 'form-control',
                    'type': 'date',
                    'placeholder': 'Select a date',
                }
            ),
            "reservation_slot": forms.Select(
                attrs={
                    'id': 'reservation_slot',
                    'class': 'form-control',
                },
            )
        }



