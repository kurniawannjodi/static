from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ContactUs
from .forms import *
# Create your views here.
def homepage(request):
    return render(request, 'division/index.html',)


def simpanContactUs(request):
    if request.method == 'POST':
        namas  = request.POST['nama']
        emails  = request.POST['email']
        no_telepons  = request.POST['no_telepon']
        subyeks  = request.POST['subyek']
        pesans  = request.POST['pesan']

        ContactUs.objects.create(nama= namas, email= emails, no_telepon= no_telepons, subyek= subyeks, pesan=pesans)
        return HttpResponse('')
