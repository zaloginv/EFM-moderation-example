from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from blog_app.models import Blog
from .forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth_app/register.html'
    success_url = reverse_lazy('auth-app:profile')

    def form_valid(self, form):
        response = super().form_valid(form)

        user = authenticate(
            self.request,
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1'),
        )

        login(request=self.request, user=user)
        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'auth_app/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['view'].request.user
        context['blogs'] = Blog.objects.filter(author=user)
        return context


class AuthLogoutView(LogoutView):
    template_name = 'auth_app/logout.html'


class AuthLoginView(LoginView):
    template_name = 'auth_app/login.html'