from django import forms
from . import models

class CalculateGpu(forms.ModelForm):
    class Meta:
        model = models.Calculator
        fields = ["mhs", "power", "price", "kwh_price"]
