from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("firstapplication/", include("firstapplication.urls")),
    path("admin/", admin.site.urls),
]