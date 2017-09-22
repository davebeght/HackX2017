from django.db import models
from django.utils import timezone
import os, collections
import numpy as np
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.core.files import File
import glob
from pprint import pprint

fs = FileSystemStorage(location="static")

class Keyword(models.Model):
  keyword_name = models.CharField(max_length=200)

class Article_Node(models.Model):
  level = models.IntegerField()
  title = models.CharField(max_length=200)
  keywords = models.ManyToManyField(Keyword, blank=True, null=True)
  text = models.CharField(max_length=5000)
  dependent_node = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

