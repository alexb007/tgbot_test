from rest_framework import viewsets

from core.api.serializers import WebsiteSerializer
from core.models import Website


class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
