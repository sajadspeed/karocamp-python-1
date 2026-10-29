from django.urls import path

from .views import index, test_page

urlpatterns = [
    path("", index, name="index"),
    path("test", test_page, name="test"),
]
