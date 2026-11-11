from django.db import models
from django.conf import settings
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="نام تگ")
    def __str__(self): return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="نویسنده")
    content = models.TextField(verbose_name="محتوا")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="تگ‌ها")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f"پست از {self.author.username}"
    
    def get_absolute_url(self):
        return reverse('social:post_detail', kwargs={'pk': self.pk})
    
    @property
    def like_count(self): return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="نویسنده")
    content = models.TextField(verbose_name="متن کامنت")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"کامنت {self.author.username}"

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta: unique_together = ('post', 'user')
