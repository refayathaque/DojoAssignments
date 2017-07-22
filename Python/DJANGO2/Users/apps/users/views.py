from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    return render(request, 'users/index.html')
