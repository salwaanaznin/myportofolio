from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Rute aplikasi didaftarkan sekali karena main.urls sudah menentukan setiap prefix.
    path("", include("main.urls")),
]