from django.db import models
from django.utils import timezone
import os, collections
import numpy as np
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.core.files import File
import glob
from pprint import pprint
import json
from django.contrib.auth.models import User

fs = FileSystemStorage(location="static")

class Profile(models.Model):
  user = models.OneToOneField(User)
  first_name = models.CharField("Vorname", max_length=30)
  last_name = models.CharField("Nachname", max_length=50)
  email = models.EmailField("E-Mail")

class Keyword(models.Model):
  keyword_name = models.CharField(max_length=200)

  def __str__(self):
    return self.keyword_name

class Article_Node(models.Model):
  level = models.IntegerField()
  title = models.CharField(max_length=200)
  keywords = models.ManyToManyField(Keyword, blank=True, null=True)
  text = models.TextField(max_length=5000)
  dependent_node = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

  def get_children(self):
    return Article_Node.objects.filter(dependent_node=self)

  def generate_json(self):
    if self.level == 1:
      children = self.get_children()
      return json.dumps({"name": self.title, "id": self.id, "inhalt": self.text, "expand": True, "children": [c.generate_json() for c in children]})
    elif self.level == 2:
      return {"name": self.title, "id": self.id, "inhalt": self.text, "expand": True}

  def __str__(self):
    return self.title + " " + str(self.level)

class Profile_Keyword_Count(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  keyword = models.ForeignKey(Keyword, on_delete=models.SET_NULL, null=True)
  count = models.FloatField()

def init_keyword_count(user):
  for keyword in Keyword.objects.all():
    Profile_Keyword_Count(user=user, keyword=keyword, count=0.0).save()
