from .models import *
from django import forms


class BuyTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('purchased_ticket', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class BookTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('purchased_ticket', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)


# class PostMessageForm(forms.Form):
#     email = forms.EmailField()
