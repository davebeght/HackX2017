from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import numpy as np
import math
from pprint import pprint


""" VIEWS """

def index(request):
  context = {}
  return render(request, 'survey/index.html', context)