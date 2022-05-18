from django.db import models

from users.models import User


class Phrase(models.Model):
    """Phrase or word in one language."""

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

    def __str__(self):
        return f"{self.phrase}: {self.language}"


class TranslationsStack(models.Model):
    """Collection of phrases with the same meaning in different languages."""

    created_at = models.DateField('Created at', auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='translations',
    )
    phrases = models.ManyToManyField(
        to='Phrase',
        through='PhraseTranslation',
        related_name='translations',
        verbose_name='Phrases',
    )


class PhraseTranslation(models.Model):
    phrase = models.ForeignKey(Phrase, on_delete=models.CASCADE)
    translation = models.ForeignKey(TranslationsStack, on_delete=models.CASCADE)
