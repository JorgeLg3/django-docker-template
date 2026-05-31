from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("pages.urls")),
    path("health/", include("healthcheck.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("auth/", include("accounts.urls")),
    path("admin/", admin.site.urls),
]
