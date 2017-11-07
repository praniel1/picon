from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from . models import UserProfile


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home_page:index'))
    else:
        try:
            userprofile = UserProfile.objects.get(userim = request.user)
        except:
            userprofile = request.user
        context = {
        'userprofile' : userprofile
        }
        return render(request, 'dash/index.html', context)

def upload_pic(request):
    pic = request.POST['pic']
    p = UserProfile(userim=request.user, avatar=pic)
    p.save()
    return redirect('dash:index')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home_page:index'))