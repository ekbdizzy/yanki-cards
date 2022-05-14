from django.db import models

from users.models import User


class Phrase(models.Model):
    """Model is for savings new words."""

    LANGUAGES = (
        ('en', 'english'),
        ('ru', 'russian'),
        ('tr', 'turkish'),
    )

    phrase = models.CharField('phrase', max_length=60, db_index=True)
    language = models.CharField(
        'Language',
        choices=LANGUAGES,
        max_length=2,
        default='ru',
    )
    users = models.ManyToManyField(
        User,
        through='UserPhrase',
        related_name='phrases',
    )

    def __str__(self):
        return f"{self.phrase}: {self.language}"


class UserPhrase(models.Model):
    """Additional model to link words and users.
    Implemented as a separate model
    to save date of creation new words by user."""

    created_at = models.DateField('Created at', auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
    )
    phrase = models.ForeignKey(
        Phrase,
        on_delete=models.CASCADE,
        verbose_name='Phrase',
    )
