from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum


def home(request):
    return render(request, 'portfolio/home.html',
                  {'portfolio': home})


def about_us(request):
    return render(request, 'portfolio/about_us.html',)


def catering(request):
    return render(request, 'portfolio/catering.html',)


def contact_us(request):
    if request.method == "POST":
        form = ResForm(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.save()
            reses = Reservation.objects.filter()
            return render(request, 'portfolio/thanks2.html',
                          {'reses': reses})
    else:
        form = ResForm()
    return render(request, 'portfolio/contact_us.html', {'form': form})


def events(request):
    if request.method == "POST":
        form = FundForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            funds = Fundraiser.objects.filter()
            return render(request, 'portfolio/thanks.html',
                          {'funds': funds})
    else:
        form = FundForm()
    return render(request, 'portfolio/events.html', {'form': form})


def menu(request):
    return render(request, 'portfolio/menu.html',)


def specials(request):
    return render(request, 'portfolio/specials.html',)


def thanks(request):
    return render(request, 'portfolio/thanks.html')

