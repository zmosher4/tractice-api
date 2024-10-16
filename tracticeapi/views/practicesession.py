from rest_framework import viewsets, serializers
from tracticeapi.models import PracticeSession
from .user import UserSerializer
from .show import ShowSerializer


class PracticeSessionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    show = ShowSerializer()

    class Meta:
        model = PracticeSession
        fields = ['id', 'session_date', 'show', 'notes', 'user']


class PracticeSessionViewSet(viewsets.ModelViewSet):
    queryset = PracticeSession.objects.all()
    serializer_class = PracticeSessionSerializer
    pagination_class = None
