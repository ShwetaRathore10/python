from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("about/", views.about),
    path("contact/", views.contact),
    path("service/", views.service),
    path("register/", views.register),
    path("login/", views.login),
    path("myadmin/", include('myadmin.urls')),
    path("user/", include('user.urls'))
]
