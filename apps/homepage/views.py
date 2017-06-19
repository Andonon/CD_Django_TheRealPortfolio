# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')
def projects(request):
    return render(request, 'homepage/projects.html')
def about(request):
    return render(request, 'homepage/about.html')
def testimonials(request):
    return render(request, 'homepage/testimonials.html')

