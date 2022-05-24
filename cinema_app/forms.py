from .models import *
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)
