from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    template_name = 'home.html'

