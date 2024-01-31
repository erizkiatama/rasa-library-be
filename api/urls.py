from django.urls import path, include

from .views import health_check


urlpatterns = [
    path("healthcheck/", health_check),
    path("book/", include("book.urls"))
]
