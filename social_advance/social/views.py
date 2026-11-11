from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, View
from .models import Post, Tag, Like, Comment
from users.models import CustomUser
from .forms import PostForm, CommentForm

# --- LIST VIEWS ---
class PostListView(ListView):
    model = Post
    template_name = 'social/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        qs = Post.objects.select_related('author').prefetch_related('tags', 'likes', 'comments')
        sort = self.request.GET.get('sort', 'desc')
        return qs.order_by('created_at') if sort == 'asc' else qs.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', 'desc')
        context['page_title'] = 'پست‌ها'
        return context

class PostListByTagView(PostListView):
    def get_queryset(self):
        self.tag_obj = get_object_or_404(Tag, name=self.kwargs['tag_name'])
        return super().get_queryset().filter(tags=self.tag_obj)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"پست‌های مرتبط با #{self.kwargs['tag_name']}"
        return context

class PostListByAuthorView(PostListView):
    def get_queryset(self):
        self.author_obj = get_object_or_404(CustomUser, username=self.kwargs['username'])
        return super().get_queryset().filter(author=self.author_obj)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"پست‌های {self.kwargs['username']}"
        return context


# --- DETAIL VIEW ---
class PostDetailView(DetailView):
    model = Post
    template_name = 'social/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return super().get_queryset().select_related('author').prefetch_related(
            'tags', 
            'likes__user', 
            'comments__author'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        
        # Sort comments from newest to oldest
        context['comments'] = post.comments.all().order_by('-created_at')
        context['comment_form'] = CommentForm()
        
        context['user_has_liked'] = False
        if self.request.user.is_authenticated:
            context['user_has_liked'] = post.likes.filter(user=self.request.user).exists()
            
        return context


# --- CREATE VIEWS (Protected by LoginRequiredMixin) ---
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'social/create_post.html'
    
    def form_valid(self, form):
        # Assign the current user as the author before saving
        form.instance.author = self.request.user
        response = super().form_valid(form)
        
        # Process and assign tags
        tags_str = form.cleaned_data.get('tags_input', '')
        if tags_str:
            for name in [t.strip() for t in tags_str.split(',') if t.strip()]:
                tag, _ = Tag.objects.get_or_create(name=name)
                self.object.tags.add(tag)
                
        return response

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('social:post_detail', kwargs={'pk': self.kwargs['pk']})
        
    def form_invalid(self, form):
        # Redirect back to the post detail page on validation error
        return redirect('social:post_detail', pk=self.kwargs['pk'])


# --- ACTION VIEW ---
class PostLikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            like.delete() # Toggle: remove like if it already exists
            
        # Redirect back to the referring page
        return redirect(request.META.get('HTTP_REFERER', 'social:post_list'))
