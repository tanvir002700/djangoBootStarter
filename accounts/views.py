from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import LoginForm
from django.http.response import HttpResponse


def home(request):
    return render(request, 'home.html')


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
            return redirect('home')
        else:
            return HttpResponse("Form is not valid")