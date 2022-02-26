from django.conf import settings
from django.core.mail import EmailMultiAlternatives

EMAIL_HOST_USER = settings.EMAIL_HOST_USER


def mail_creator(emails, context):
    subject = 'New notification!'

    message_alternatives = EmailMultiAlternatives(
        subject=subject,
        body=context,
        from_email=EMAIL_HOST_USER,
        to=emails
    )

    message_alternatives.send()
