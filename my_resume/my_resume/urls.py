from django.contrib import admin
from django.urls import path
from resume import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('resume/', views.resume_view, name='resume'),
    path('', views.login_view, name='home'),  # مسیر پیش‌فرض برای ریشه
]

