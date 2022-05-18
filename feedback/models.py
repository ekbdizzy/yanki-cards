from django.db import models

from users.models import User


class Feedback(models.Model):
    """Feedback from users. Any problems, suggestions and other questions."""

    class Meta:
        verbose_name_plural = 'Feedback'

    FEEDBACK_STATUSES = (
        ('new', 'New'),
        ('important', 'Important'),
        ('active', 'Active'),
        ('closed', 'Closed'),
    )

    THEMES = (
        ('problem', "I have a problem"),
        ('suggestion', "I'd like to suggest you"),
        ('thanks', "I just want to thank you"),
        ('other', 'other'),
    )

    theme = models.CharField(
        'Title',
        choices=THEMES,
        max_length=60,
    )

    title = models.CharField(
        'Title',
        max_length=60,
    )

    text = models.TextField('Text', max_length=400, default='')
    status = models.CharField(
        'Status',
        choices=FEEDBACK_STATUSES,
        max_length=20,
    )

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    edited_at = models.DateTimeField('Edited at', auto_now=True)

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user',
        verbose_name='User',
    )

    def __str__(self):
        return f"{self.status} {self.theme} {self.title}"
