from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter

from .views import PacksViewSet, PackIconsViewSet

router = DefaultRouter()

router.register('packs', PacksViewSet)
router.register('packicons', PackIconsViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
