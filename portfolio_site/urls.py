from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("qr/<slug:service>.png", views.qr_code, name="qr_code"),
]
