from rest_framework import serializers

from core.models import YTData


class YTDataSerializer(serializers.ModelSerializer):
    '''
    YTData Serializer
    '''

    class Meta:
        model = YTData
        fields = '__all__'