"""uwe_flix URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import user_page.views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("user_page.urls")),
    path('admin/', admin.site.urls),

    path('upload_details', views.upload_details_page, name="upload_details"),
    path('upload_movie', views.movie_details, name="upload_movie"),            # Upload section, added by Radiela
    path('upload_screen', views.screen_details, name="upload_screen"),
    path('upload_showing', views.showing_details, name="upload_showing"),

    path('show_movies', views.display_movie_details, name="show_movies"),            # Display section, added by Radiela
    path('showings', views.display_showing_details, name="showings"),
    path('show_screens', views.display_screen_details, name="show_screens"),
    path('show_upcoming', views.display_upcoming, name="show_upcoming"),

    path('payment/', views.display_payment, name="payment"),     # Payment section added by Radiela
    path('payment_page', views.display_payment_page, name="payment_page"),

    path('login/', views.login_user, name="login"),
    path("logout/", views.logout_user, name ="logout"),

    path("staff_registration", views.staff_registration, name = "staff_registration"),
    path("club_registration", views.club_registration, name = "club_registration"),
    path("student_registration", views.student_registration, name = "student_registration"),

    path("manager/", views.manager, name = "manager"),
    path("accounts/", views.accounts, name = "accounts"),  # added by Radiela
    path("show_club/<club_id>", views.show_club, name = "show_club"),
    path("show_student/<student_id>", views.show_student, name = "show_student"),
    
    path("shopping_cart", views.shopping_cart, name="shopping_cart")]  # added by Radiela

urlpatterns += staticfiles_urlpatterns()   # Load static files, added by Radiela

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # Load images, added by Radiela

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)   # added by Radiela