from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from album.models import Photo
from album.serializers import PhotoSerializer
from album.permissions import IsSelf


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        check_user_viewed = Photo.objects.filter(id=instance.id, viewed_by=request.user)
        if not check_user_viewed:
            instance.viewed_by.add(request.user)
            instance.views += 1
            instance.save()
        return Response(serializer.data)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsSelf]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

