from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('coaches/', views.coaches, name='coaches'),
    path('rockstar-internal-ctrl/', views.enquiry_dashboard, name='dashboard'),
    path('rockstar-access/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('rockstar-exit/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
