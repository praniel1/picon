# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.admin import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'home_page/index.html')
    else:
        return HttpResponseRedirect(reverse('dash:index'))


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('dash:index'))

def register(request):
    template = 'home_page/dash.html'
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['pass']
    email = request.POST['mail']
    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password,
                                    email=email)
    user.save()
    # return redirect('home_page:dash')
    return HttpResponseRedirect(reverse('dash:dashboard'))