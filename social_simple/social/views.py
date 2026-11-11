from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post, Tag, Like
from users.models import CustomUser
from .forms import PostForm, CommentForm

def get_paginated_posts(request, queryset):
    sort = request.GET.get('sort', 'desc')
    if sort == 'asc':
        queryset = queryset.order_by('created_at')
    else:
        queryset = queryset.order_by('-created_at')
        
    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj, sort

def post_list(request):
    page_obj, current_sort = get_paginated_posts(request, Post.objects.all())
    return render(request, 'social/post_list.html', {
        'page_obj': page_obj, 
        'current_sort': current_sort,
        'page_title': 'پست‌ها'
    })

def post_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    page_obj, current_sort = get_paginated_posts(request, Post.objects.filter(tags=tag))
    return render(request, 'social/post_list.html', {
        'page_obj': page_obj, 
        'current_sort': current_sort,
        'page_title': f'پست‌های مرتبط با #{tag_name}'
    })

def post_by_author(request, username):
    author = get_object_or_404(CustomUser, username=username)
    page_obj, current_sort = get_paginated_posts(request, Post.objects.filter(author=author))
    return render(request, 'social/post_list.html', {
        'page_obj': page_obj, 
        'current_sort': current_sort,
        'page_title': f'پست‌های {author.username}'
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')
    
    # Check if current user has liked this post
    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = post.likes.filter(user=request.user).exists()

    return render(request, 'social/post_detail.html', {
        'post': post, 
        'comments': comments, 
        'comment_form': CommentForm(),
        'user_has_liked': user_has_liked
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            tags_str = form.cleaned_data.get('tags_input', '')
            if tags_str:
                for name in [t.strip() for t in tags_str.split(',') if t.strip()]:
                    tag, _ = Tag.objects.get_or_create(name=name)
                    post.tags.add(tag)
            return redirect('social:post_list')
    else:
        form = PostForm()
    return render(request, 'social/create_post.html', {'form': form})

@login_required
def like_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            like.delete()
    return redirect(request.META.get('HTTP_REFERER', 'social:post_list'))

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
    return redirect('social:post_detail', pk=post.pk)
