from django.shortcuts import render
from django.http import HttpResponse
from .models import login
# Create your views here.
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
   if request.method == 'POST':
      username1 = request.POST['email']
      password1 = request.POST['pas']

      newlogin = login(username=username1, password=password1)
      newlogin.save()

      
   return render(request,"home.html", {})

