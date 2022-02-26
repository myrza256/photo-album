from celery import shared_task

from album.models import Photo, NotificationText
from album.utils import mail_creator


@shared_task
def send_message() -> bool:
    text = NotificationText.load().notification_text
    emails = list(set([photo.creator.email for photo in Photo.objects.all().order_by('-views')[:3] if photo]))

    if emails:
        context = {
            'text': text
        }

        mail_creator(emails, context)
        return True
    return False
