from rest_framework import viewsets, serializers, status
from tracticeapi.models import Show, Artist
from .user import UserSerializer
from .artist import ArtistSerializer
from rest_framework.response import Response
import logging


class ShowSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    artist = ArtistSerializer()

    class Meta:
        model = Show
        fields = ['id', 'description', 'performance_date', 'user', 'artist']


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    pagination_class = None

    def create(self, request):
        new_show = Show()
        new_show.description = request.data['description']
        new_show.performance_date = request.data['performance_date']
        new_show.artist = Artist.objects.get(pk=request.data['artist_id'])
        new_show.user = request.user
        new_show.save()

        serializer = ShowSerializer(new_show, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        logger = logging.getLogger(__name__)

        logger.info(f"Starting update for show {pk}")
        logger.info(f"Request data: {request.data}")

        try:
            show = Show.objects.get(pk=pk)
            logger.info(f"Found show {pk}")

            show.description = request.data.get('description', show.description)
            show.performance_date = request.data.get(
                'performance_date', show.performance_date
            )

            if 'artist_id' in request.data:
                artist = Artist.objects.get(pk=request.data['artist_id'])
                show.artist = artist
                logger.info(f"Updated artist to {artist.id}")

            show.user = request.user
            logger.info("About to save show")
            show.save()
            logger.info(f"Successfully saved show {pk}")

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            logger.error(f"Error updating show {pk}: {str(e)}")
            return Response(
                {'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
