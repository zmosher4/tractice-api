from rest_framework import viewsets, serializers, status
from tracticeapi.models import Artist
from .user import UserSerializer
from rest_framework.response import Response


class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Artist
        fields = ['id', 'name', 'user']


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = None

    def create(self, request):
        new_artist = Artist()
        new_artist.name = request.data['name']
        new_artist.user = request.user
        new_artist.save()

        serializer = ArtistSerializer(new_artist, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        artist = Artist.objects.get(pk=pk)
        artist.name = request.data['name']
        artist.user = request.user
        artist.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
