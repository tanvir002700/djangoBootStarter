from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from .forms import LoginForm, RegisterForm
from django.http.response import HttpResponse
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth import login


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        user = form.save()
        if user:
            return redirect(reverse('accounts:login'))
        else:
            return HttpResponse("Form is not valid")


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        user = form.authenticate()
        if user:
            login(request, user)
            return redirect(reverse('dashboard:home'))
        else:
            return HttpResponse("Form is not valid")


class LogoutView(RedirectView):
    url = '/accounts/login'

    def get_redirect_url(self, *args, **kwargs):
        print(self.request.user.is_authenticated())
        if self.request.user.is_authenticated():
            print("going to logout")
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)
