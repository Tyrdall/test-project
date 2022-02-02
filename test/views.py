from django.http.response import JsonResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


def api(request):
    return JsonResponse({
        'data': [
            {'title': 'left', 'color': '#837cdf'},
            {'title': 'mid', 'color': '#7c83df'},
            {'title': 'right', 'color': '#df7c83'},
        ],
    })
