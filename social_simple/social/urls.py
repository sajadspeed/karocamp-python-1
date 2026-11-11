from django.urls import path
from . import views

app_name = 'social'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<str:tag_name>/', views.post_by_tag, name='post_by_tag'),
    path('author/<str:username>/', views.post_by_author, name='post_by_author'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
]
