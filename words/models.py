from django.db import models

from users.models import User


class Word(models.Model):
    """Model is for savings new words."""

    LANGUAGES = (
        ('en', 'english'),
        ('ru', 'russian'),
    )

    word = models.CharField('Word', max_length=60, db_index=True)
    language = models.CharField(
        'Language',
        choices=LANGUAGES,
        max_length=2,
        default='ru',
    )
    users = models.ManyToManyField(
        User,
        through='UserWord',
        related_name='words',
    )

    def __str__(self):
        return f"{self.word}: {self.language}"


class UserWord(models.Model):
    """Additional model to link words and users.
    Implemented as a separate model
    to save date of creation new words by user."""

    created_at = models.DateField('Created at', auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
    )
    word = models.ForeignKey(
        Word,
        on_delete=models.CASCADE,
        verbose_name='Word',
    )
