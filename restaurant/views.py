from django.shortcuts import render
from django.views import generic
from .models import Reservation
from django.shortcuts import render
from .forms import Reserve_table_form
from django.contrib import messages


# Create your views here.
def get_index(request):
    return render(request, 'restaurant/index.html')


def get_menu(request):
    return render(request, 'restaurant/menu.html')


def get_base(request):
    return render(request, 'restaurant/base.html')


def get_book(request):
    if request.POST:
        form = Reserve_table_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking succesful!')
    return render(request, 'restaurant/book.html', {'form': Reserve_table_form})
