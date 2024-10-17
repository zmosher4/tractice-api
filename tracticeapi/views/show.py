from rest_framework import viewsets, serializers, status
from tracticeapi.models import Show
from .user import UserSerializer
from rest_framework.response import Response


class ShowSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Show
        fields = ['id', 'description', 'performance_date', 'user']


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    pagination_class = None

    def create(self, request):
        new_show = Show()
        new_show.description = request.data['description']
        new_show.performance_date = request.data['performance_date']
        new_show.user = request.user
        new_show.save()

        serializer = ShowSerializer(new_show, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        show = Show.objects.get(pk=pk)
        show.description = request.data['description']
        show.performance_date = request.data['performance_date']
        show.user = request.user
        show.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
