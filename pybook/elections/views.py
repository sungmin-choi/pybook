# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, 'elections/index.html')


def login(request):
    return render(request, 'elections/login.html')


def join(request):
    return render(request, 'elections/join.html')


def search(request):
    searching = request.GET.get('searching')
    return render(request, 'elections/search.html', {'searching': searching})


def userDetail(request):
    return render(request, 'elections/userDetail.html')


def logout(request):
    return redirect(reverse("home"))
