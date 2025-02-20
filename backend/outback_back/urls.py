from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/outback_products/", include("outback_products.urls")),
    path("api/v1/outback_accounts/", include("outback_accounts.urls")),
]