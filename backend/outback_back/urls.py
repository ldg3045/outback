from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/v1/outback_main/", include("outback_main.urls")),
    path("api/v1/outback_accounts/", include("outback_accounts.urls")),
]