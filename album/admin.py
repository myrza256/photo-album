from django.contrib import admin

from album.models import Photo, NotificationText

admin.site.register(Photo)
admin.site.register(NotificationText)