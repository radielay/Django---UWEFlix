from .views import *
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import user_page.views as views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),

    path('contact_page', views.dislpay_contact_page, name="contact_page"),  # Contact support team, 
    path('contact_form', views.contact_form, name="contact_form"),          # added by Radiela

    path("user_registration", views.user_registration, name="user_registration"),  # added by Radiela
    path('registration_successful', views.registration_successful, name="registration_successful"), # added by Radiela
    path('logged_in', views.auth_user, name="logged_in"),  # added by Radiela
    path('forgotten_password', views.password_request, name="forgotten_password"),  # added by Radiela
    path('password_changed', views.password_changed, name="password_changed"),  # added by Radiela
    path('add_credits', views.display_add_credits, name="add_credits"),  # added by Radiela
    path('create_order', views.create_order, name="create_order"),  # added by Radiela
    path('forgotten_username', views.forgotten_username, name="forgotten_username"),  # added by Radiela
    path('id_changed', views.username_changed, name="id_changed"),   # added by Radiela
    path('upload_upcoming', views.upcoming_movie_details, name="upload_upcoming"),  # added by Radiela
    path('monthly_payments', views.monthly_payments, name="monthly_payments"),   # added by Radiela
]