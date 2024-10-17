from rest_framework import viewsets, serializers, status
from tracticeapi.models import ShowSong, Show, Song
from .song import SongSerializer
from .show import ShowSerializer
from rest_framework.response import Response


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

    def create(self, request):
        show_song = ShowSong()
        show_song.show = Show.objects.get(pk=request.data['show_id'])
        show_song.song = Song.objects.get(pk=request.data['song_id'])
        show_song.save()

        serializer = ShowSongSerializer(show_song, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        show_song = ShowSong.objects.get(pk=pk)
        show_song.show = Show.objects.get(pk=request.data['show_id'])
        show_song.song = Song.objects.get(pk=request.data['song_id'])
        show_song.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
