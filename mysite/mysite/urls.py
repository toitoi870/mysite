from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path("trade/", include("trade.urls")),
    path('admin/', admin.site.urls),
]
