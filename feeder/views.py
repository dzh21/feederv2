# -*- coding: utf-8 -*-
from django.shortcuts import render

def home(request):
    return render(request, "feeder/index.html", {})

def home_files(request, filename):    
    return render(request, filename, {}, content_type="text/plain")

