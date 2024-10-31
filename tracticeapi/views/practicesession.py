from rest_framework import viewsets, serializers, status
from tracticeapi.models import PracticeSession, Show
from .user import UserSerializer
from .show import ShowSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response


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

    def create(self, request):
        new_session = PracticeSession()
        new_session.session_date = request.data['session_date']
        new_session.show = Show.objects.get(pk=request.data['show_id'])
        new_session.notes = request.data['notes']
        new_session.user = request.user
        new_session.save()

        serializer = PracticeSessionSerializer(
            new_session, context={'request': request}
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        practice_session = PracticeSession.objects.get(pk=pk)
        practice_session.session_date = request.data['session_date']
        practice_session.show = Show.objects.get(pk=request.data['show_id'])
        practice_session.notes = request.data['notes']
        practice_session.user = request.user
        practice_session.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
