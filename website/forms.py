from django import forms
from . import models


class CRMForm(forms.ModelForm):
    class Meta:
        model = models.ModelCRM
        fields = ["first_name", "last_name", "email", "address", "city", "province", "postal_code"]