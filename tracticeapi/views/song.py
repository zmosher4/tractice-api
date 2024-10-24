from rest_framework import viewsets, serializers, status
from tracticeapi.models import Song
from rest_framework.response import Response


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['id', 'title', 'description']


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = None

    def create(self, request):
        song = Song()
        song.title = request.data['title']
        song.description = request.data['description']
        song.save()

        serializer = SongSerializer(song, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        song = Song.objects.get(pk=pk)
        song.title = request.data['title']
        song.description = request.data['description']
        song.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
