from django.urls import path
from rest_framework.routers import DefaultRouter

from core.viewsets import YTDataViewSet


urlpatterns = [

]

router = DefaultRouter()
router.register('youtube-data', YTDataViewSet, 'youtube-data')
urlpatterns += router.urls
