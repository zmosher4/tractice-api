from rest_framework import viewsets, serializers
from tracticeapi.models import ShowSong
from .song import SongSerializer
from .show import ShowSerializer


class ShowSongSerializer(serializers.ModelSerializer):
    song = SongSerializer()
    show = ShowSerializer()

    class Meta:
        model = ShowSong
        fields = ['id', 'show', 'song']


class ShowSongViewSet(viewsets.ModelViewSet):
    queryset = ShowSong.objects.all()
    serializer_class = ShowSongSerializer
    pagination_class = None
