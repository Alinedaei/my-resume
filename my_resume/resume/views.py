# resume/views.py

from django.shortcuts import render
from .models import Resume

def home(request):
    resume = Resume.objects.first()  # فرض می‌کنیم فقط یک رزومه داریم
    return render(request, 'index.html', {'resume': resume})

