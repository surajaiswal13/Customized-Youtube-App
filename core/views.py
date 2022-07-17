from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import YTData


# Create your views here.

class YTDataSearchAPIView(APIView):
    '''
    ApiView for Searching based on Title and
        Description
    '''

    def post(self, request):

        title = request.data.get('title')
        description = request.data.get('description')

        result = YTData.objects.filter(title__icontains=title, description__icontains=description)

        response_list = [
            {
                "id": item.id,
                "title": item.title,
                "description": item.description,
                "published_at": item.published_at,
                "thumbnail_url_default": item.thumbnail_url_default,
                "thumbnail_url_medium": item.thumbnail_url_medium,
                "thumbnail_url_high": item.thumbnail_url_high
            }

            for item in result
        ]

        return Response(response_list)