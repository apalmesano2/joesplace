from django import forms
from .models import Fundraiser, Reservation


class FundForm(forms.ModelForm):
    class Meta:
        model = Fundraiser
        fields = ('firstName', 'lastName', 'email', 'phone', 'pref_contact', 'org', 'fund_type')
        labels = {
            'firstName': 'First Name',
            'lastName': 'Last Name',
            'email': 'Email',
            'phone': 'Phone Number',
            'pref_contact': 'Preferred Contact Method',
            'org': 'Organization',
            'fund_type': 'Fundraiser Type You Are Most Interested In'
        }


class ResForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('firstName', 'lastName', 'phone', 'partySize', 'dateOfRes', 'time')
        labels = {
            'firstName': 'First Name',
            'lastName': 'Last Name',
            'phone': 'Phone',
            'partySize': 'Party Size (max. 10)',
            'dateOfRes': 'Date (please enter as YYYY-MM-DD)',
            'time': 'Time',
        }
