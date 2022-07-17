from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter

from core.models import YTData
from core.serializers import YTDataSerializer


class YTDataViewSet(viewsets.ModelViewSet):
    '''
    Viewset for getting Youtube Data from Database sorted 
        in reverse chronological order of their publishing date-time
    '''

    queryset = YTData.objects.all().order_by("-published_at")
    serializer_class = YTDataSerializer
    http_method_names = ['get']
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['id', 'title']
    search_fields = ['title', 'short_description', 'description']
