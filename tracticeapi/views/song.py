from rest_framework import viewsets, serializers
from tracticeapi.models import Song
from .artist import ArtistSerializer


class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'description']


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = None
