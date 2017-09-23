from .models import *

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
  first_name = forms.CharField()
  last_name = forms.CharField()
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ('username', 'email', 'password1')

#  def __init__(self, *args, **kwargs):
#    super().__init__(*args, **kwargs)
#    del self.fields['password2']