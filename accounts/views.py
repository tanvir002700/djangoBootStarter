from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from .forms import LoginForm, RegisterForm, ProfileUpdateForm
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth import login
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        user = form.save()
        if user:
            return redirect(reverse('accounts:login'))
        else:
            return render(request, self.template_name, {'form': form})


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        print(form)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        user = form.authenticate()
        if user:
            if request.POST.get('remember') is not None:
                self.request.session.set_expiry(0)
            login(request, user)
            return redirect(reverse('dashboard:home'))
        else:
            form.errors['failed'] = 'authentication failed'
            return render(request, self.template_name, {'form': form})


class LogoutView(RedirectView):
    url = '/accounts/login'

    def get_redirect_url(self, *args, **kwargs):
        print(self.request.user.is_authenticated())
        if self.request.user.is_authenticated():
            print("going to logout")
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'accounts:login'
    template_name = 'profile_update.html'
    form_class = ProfileUpdateForm

    def get_success_url(self):
        return reverse('dashboard:home')

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDetailView(LoginRequiredMixin, DetailView):
    login_url = 'accounts:login'
    template_name = 'profile_details.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user
