from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.utils import timezone


PREF_CONTACT = [
    ('Email', 'Email'),
    ('Phone', 'Phone'),
    ]

FUND_TYPES = [
    ('Pizza Night', 'Pizza Night'),
    ('Joe\'s Money', 'Joe\'s Money'),
    ('School Fundraiser', 'School Fundraiser'),
    ('Other', 'Other')
]

TIMES = [
    (datetime.time(10, 30, 0), '10:30 AM'),
    (datetime.time(11, 0, 0), '11:00 AM'),
    (datetime.time(11, 30, 0), '11:30 AM'),
    (datetime.time(12, 0, 0), '12:00 PM'),
    (datetime.time(12, 30, 0), '12:30 PM'),
    (datetime.time(13, 0, 0), '1:00 PM'),
    (datetime.time(13, 30, 0), '1:30 PM'),
    (datetime.time(14, 0, 0), '2:00 PM'),
    (datetime.time(14, 30, 0), '2:30 PM'),
    (datetime.time(15, 0, 0), '3:00 PM'),
    (datetime.time(15, 30, 0), '3:30 PM'),
    (datetime.time(16, 0, 0), '4:00 PM'),
    (datetime.time(16, 30, 0), '4:30 PM'),
    (datetime.time(17, 0, 0), '5:00 PM'),
    (datetime.time(17, 30, 0), '5:30 PM'),
    (datetime.time(18, 0, 0), '6:00 PM'),
    (datetime.time(18, 30, 0), '6:30 PM'),
    (datetime.time(19, 0, 0), '7:00 PM'),
    (datetime.time(19, 30, 0), '7:30 PM'),
    (datetime.time(20, 0, 0), '8:00 PM'),
    (datetime.time(20, 30, 0), '8:30 PM'),
    (datetime.time(21, 0, 0), '9:00 PM'),
    (datetime.time(21, 30, 0), '9:30 PM'),
]


class Fundraiser(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=10)
    pref_contact = models.CharField(max_length=50, choices=PREF_CONTACT)
    org = models.CharField(max_length=200)
    fund_type = models.CharField(max_length=200, choices=FUND_TYPES)


class Reservation(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    partySize = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    dateOfRes = models.DateField()
    time = models.TimeField(choices=TIMES)
