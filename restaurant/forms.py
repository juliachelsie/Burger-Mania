from django.forms import ModelForm
from django import forms
from .models import Reservation

tableChoices = {
    'window1': 'Bigger table by window',
    'window2': 'Smaller table by window',
    'bigTable1': 'Big table in isle',
    'bigTable2': 'Big table upstairs'
}

sittingTimes = [('3-5', '15-17'), ('5-7', '17-19'), ('7-9', '19-21'),]


class Reserve_table_form(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Full Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    phone_number = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': 'Phone-number', 'style': 'width: 300px;', 'class': 'form-control'}))
    number_of_people = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Number of people', 'style': 'width: 300px;', 'class': 'form-control'}))
    date = forms.DateField(widget=forms.NumberInput(
        attrs={'placeholder': 'Which day do you wish to visit us?', 'class': 'form-control', 'type': 'date', 'style': 'width: 300px;'}))
    time = forms.ChoiceField(choices=sittingTimes, widget=forms.Select(
        attrs={'placeholder': 'What time do you want to visit us?', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone_number', 'number_of_people', 'date', 'time']
