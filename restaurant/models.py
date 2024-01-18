from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.

sittingTimes = (
    ("3-5", "15-17"),
    ("5-7", "17-19"),
    ("7-9", "19-21"),
)


class Reservation(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    phone_number = models.IntegerField()
    number_of_people = models.IntegerField(validators=[MinValueValidator(0),
                                                       MaxValueValidator(5)])
    table = models.IntegerField(null=True, blank=False, validators=[MinValueValidator(0),
                                MaxValueValidator(5)])
    date = datetime.now()
    time = models.CharField(choices=sittingTimes, max_length=25)

    def __str__(self):
        return self.name
