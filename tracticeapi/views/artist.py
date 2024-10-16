from rest_framework import viewsets, serializers
from tracticeapi.models import Artist
from .user import UserSerializer


class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Artist
        fields = ['id', 'name', 'user']


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = None
