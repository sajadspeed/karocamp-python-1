from django.urls import path

from .views import create, get_all, get, search

app_name = "students"

urlpatterns = [
    path("create/", create, name="create"),
    path("get-all/", get_all, name="get-all"),
    path("get/", get, name="get"),
    path("search/", search, name="search"),
]
