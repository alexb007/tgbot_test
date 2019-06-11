from django.shortcuts import render
from django.views.generic import ListView

from core.models import (
    Crypto,
    Website,
)


def index(request):
    return render(request, 'core/index.html')


class CryptoListView(ListView):
    model = Crypto
    context_object_name = 'currencies'
    paginate_by = 10

    def get_queryset(self):
        queryset = Crypto.objects.filter(current_rate__isnull=False).order_by('name', 'rate_changed')
        return queryset


class WebSiteListView(ListView):
    model = Website
    context_object_name = 'websites'
