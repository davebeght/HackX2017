from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import numpy as np
import math
from .forms import SignUpForm
from pprint import pprint
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import init_keyword_count


""" VIEWS """

@login_required
def index(request):
  context = {}
  return render(request, 'survey/index.html', context)

def registration(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      user.first_name = form.cleaned_data.get('first_name')
      user.last_name = form.cleaned_data.get('last_name')
      user.email = form.cleaned_data.get('email')
      user.save()
      login(request, user)
      init_keyword_count(user)
      return redirect('index')
  else:
    form = SignUpForm()
  return render(request, 'survey/registration.html', {'form': form, 'title': "Registrierung"})