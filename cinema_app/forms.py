from .models import *
from django import forms


class BuyBookTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('purchased_ticket', )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)


# class PostMessageForm(forms.Form):
#     email = forms.EmailField()
