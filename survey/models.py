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
