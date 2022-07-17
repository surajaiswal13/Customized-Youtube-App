from django.urls import path
from rest_framework.routers import DefaultRouter

from core.viewsets import YTDataViewSet
from core.views import YTDataSearchAPIView


urlpatterns = [
    path('search/', YTDataSearchAPIView.as_view(), name='search')
]

router = DefaultRouter()
router.register('youtube-data', YTDataViewSet, 'youtube-data')
urlpatterns += router.urls
