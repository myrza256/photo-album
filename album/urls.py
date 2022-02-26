from rest_framework import routers

from album.views import PhotoViewSet

router = routers.DefaultRouter()

router.register(r'albums', PhotoViewSet, basename='album')

urlpatterns = []
urlpatterns += router.urls