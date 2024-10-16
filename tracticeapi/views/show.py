from rest_framework import viewsets, serializers
from tracticeapi.models import Show
from .user import UserSerializer


class ShowSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Show
        fields = ['id', 'description', 'performance_date', 'user']


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    pagination_class = None
