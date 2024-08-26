from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # هدایت کاربر به داشبورد بعد از لاگین
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def resume_view(request):
    return render(request, 'resume.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def index_view(request):
    return render(request, 'index.html')
