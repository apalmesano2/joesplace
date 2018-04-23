from django.contrib import admin
from .models import Fundraiser, Reservation


class FundraiserList(admin.ModelAdmin):
    list_display = ('lastName', 'firstName', 'email', 'phone', 'pref_contact', 'org', 'fund_type')
    list_filter = ('lastName', 'firstName', 'email', 'phone', 'pref_contact', 'org', 'fund_type')
    search_fields = ('lastName', 'firstName', 'email', 'phone', 'pref_contact', 'org', 'fund_type')
    ordering = ['lastName', 'firstName']


class ReservationLIst(admin.ModelAdmin):
    list_display = ('lastName', 'firstName', 'phone', 'partySize', 'dateOfRes', 'time')
    list_filter = ('lastName', 'firstName', 'phone', 'partySize', 'dateOfRes', 'time')
    search_fields = ('lastName', 'firstName', 'phone', 'partySize', 'dateOfRes', 'time')
    ordering = ['dateOfRes', 'time', 'lastName', 'firstName']


admin.site.register(Fundraiser, FundraiserList)
admin.site.register(Reservation, ReservationLIst)

