from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    tags_input = forms.CharField(
        max_length=255, 
        required=False, 
        help_text='تگ‌ها را با کاما (,) جدا کنید. مثال: برنامه_نویسی, جنگو', 
        label='تگ‌ها',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثال: جنگو, آموزش'})
    )
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'چه چیزی در ذهن دارید؟'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': ''}
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'نظر خود را بنویسید...'})
        }
