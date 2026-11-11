from django.urls import path
from . import views

app_name = 'social'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<str:tag_name>/', views.PostListByTagView.as_view(), name='post_by_tag'),
    path('author/<str:username>/', views.PostListByAuthorView.as_view(), name='post_by_author'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/like/', views.PostLikeView.as_view(), name='like_post'),
    path('post/<int:pk>/comment/', views.CommentCreateView.as_view(), name='add_comment'),
]
