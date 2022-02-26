import magic

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from album.models import Photo

MAX_FILE_SIZE = 5242880
FILE_TYPES = ['image/jpeg', 'image/png', 'image/jpg']


class PhotoSerializer(serializers.ModelSerializer):

    def validate_image(self, value):

        mime_type = magic.from_buffer(value.read(), mime=True)

        if mime_type not in FILE_TYPES:
            raise ValidationError(
                {'error': ('Image mime must be: %s' % ', '.join(FILE_TYPES))}
            )
        if value.size > MAX_FILE_SIZE:
            raise ValidationError(
                {'error': ('Image size must be not more %i bytes' % MAX_FILE_SIZE)}
            )
        return value

    class Meta:
        model = Photo
        fields = ['id', 'title', 'image', 'owner', 'views']
        read_only_fields = ('created_at', 'updated_at')


