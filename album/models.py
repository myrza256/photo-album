from PIL import Image
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.BigIntegerField(default=0)
    viewed_by = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class NotificationText(models.Model):
    notification_text = models.TextField(blank=True)

    def __str__(self):
        return self.pk
