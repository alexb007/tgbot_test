from rest_framework import routers

from core.api.views import WebsiteViewSet

router = routers.DefaultRouter()
router.register(r'websites', WebsiteViewSet)
