from django.forms import ModelForm
from django import forms
from .models import Reservation


class Reserve_table_form(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Full Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    phone_number = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': 'Phone-number', 'style': 'width: 300px;', 'class': 'form-control'}))
    number_of_people = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Number of people', 'style': 'width: 300px;', 'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date', 'style': 'width: 300px;'}))
    time = forms.TimeField(widget=forms.TimeInput(
        attrs={'style': 'width: 300px;', 'class': 'form-control', 'type': 'time'}))

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone_number',
                  'number_of_people', 'date', 'time']
