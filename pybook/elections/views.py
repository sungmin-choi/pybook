# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Book
from django.db.models import Q
import json

# Create your views here.


def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'elections/index.html', context)


def login(request):
    return render(request, 'elections/login.html')


def join(request):
    return render(request, 'elections/join.html')


def search(request):
    searching = request.GET.get('searching')
    books = Book.objects.all().filter(Q(name__contains=searching)
                                      | Q(author__contains=searching))
    context = {'books': books, 'searching': searching}
    print(books)
    return render(request, 'elections/search.html', context)


def userDetail(request):
    return render(request, 'elections/userDetail.html')


def logout(request):
    return redirect(reverse("home"))
