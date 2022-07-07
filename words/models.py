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
    language_code = models.CharField(
        'Language_code',
        choices=LANGUAGES,
        max_length=2,
        default='en',
    )

    def __str__(self):
        return f"{self.phrase}: {self.language_code}"


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

    def __str__(self):
        all_phrases = [phrase for phrase in self.phrases.all()]
        phrases = " | ".join(
            (f"{phrase.phrase}: {phrase.language}" for phrase in all_phrases),
        )
        return f"{self.user}, <{phrases}>"


class PhraseTranslation(models.Model):
    phrase = models.ForeignKey(Phrase, on_delete=models.CASCADE)
    translation = models.ForeignKey(TranslationsStack, on_delete=models.CASCADE)
