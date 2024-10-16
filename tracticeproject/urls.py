from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from tracticeapi.models import *
from tracticeapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'artists', ArtistViewSet, 'artist')
router.register(r'shows', ShowViewSet, 'show')
router.register(r'songs', SongViewSet, 'song')
router.register(r'showsongs', ShowSongViewSet, 'showsong')
router.register(r'practicesessions', PracticeSessionViewSet, 'practicesession')
urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    path("api-token-auth", obtain_auth_token),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework")),
]
