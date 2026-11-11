from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthForm

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('social:post_list')

    def form_valid(self, form):
        # Save user and log them in
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthForm
    redirect_authenticated_user = True
