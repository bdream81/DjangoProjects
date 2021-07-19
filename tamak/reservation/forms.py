from django import forms
from django.forms import widgets
from .models import Reservation
from django.db.models.enums import IntegerChoices
from django.forms.widgets import DateInput, NumberInput, Textarea, TimeInput

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ["client"]
        
        widgets = {
                "date_bron": forms.DateInput(
                    attrs={
                        "class": "form-control datetimepicker-input",
                        "data-target": "#datetimepicker4",
                        "placeholder": "Date",
                        "type": "date",
                    }
                ),
                "time_bron": forms.TimeInput(
                    attrs={
                        "class": "form-control timepicker-input",
                        "data-target": "#datetimepicker3",
                        "placeholder": "Time",
                        "type": "time",
                    }
                ),
                "person": forms.Select(
                    attrs={"class": "form-control", "id": "selectPerson"}
                ),
                "comment": forms.Textarea(attrs={"cols": 30, "rows": 3}),
                "phon_number": forms.NumberInput(
                    attrs={
                        "class": "form-control number-input",
                        "placeholder": "550123456",
                        "type": "number",
                    }
                ),
            }


