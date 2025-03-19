from django import forms
from .models import Loans

class LoansForm(forms.ModelForm):
    class Meta:
        model = Loans 
        fields = ['title', 'amount','is_paid' ]


    