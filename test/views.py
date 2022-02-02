from django.http.response import JsonResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
