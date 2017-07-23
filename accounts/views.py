from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import LoginForm

def home(request):
    return render(request, 'home.html')


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
