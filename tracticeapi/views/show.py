from rest_framework import viewsets, serializers, status
from tracticeapi.models import Show, Artist
from .user import UserSerializer
from .artist import ArtistSerializer
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)


class ShowSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    artist = ArtistSerializer()

    class Meta:
        model = Show
        fields = ['id', 'description', 'performance_date', 'user', 'artist']


class ShowViewSet(viewsets.ModelViewSet):

    queryset = Show.objects.select_related('user', 'artist').all()
    # ... rest of the code    serializer_class = ShowSerializer
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
        logger.info(f"Starting update for show {pk}")
        try:
            show = Show.objects.select_related('user', 'artist').get(pk=pk)
            logger.info(f"Found show {pk}")

            # Log the incoming data
            logger.info(f"Update data: {request.data}")

            show.description = request.data['description']
            show.performance_date = request.data['performance_date']

            try:
                show.artist = Artist.objects.get(pk=request.data['artist_id'])
                logger.info(f"Found artist {request.data['artist_id']}")
            except ObjectDoesNotExist:
                logger.error(f"Artist {request.data['artist_id']} not found")
                raise ValidationError({'artist_id': 'Invalid artist ID'})

            show.user = request.user
            show.save()
            logger.info(f"Successfully updated show {pk}")

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            logger.error(f"Error updating show {pk}: {str(e)}")
            raise
