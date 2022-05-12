from django.db import models

from users.models import User


class Theme(models.Model):
    """Questions may be sorted by theme.
    This model is a list of themes for questions.
    Users can create themes by himself.
    User's created models are private."""

    title = models.CharField('Title', max_length=50, unique=True)
    is_private = models.BooleanField(default=True)
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='themes',
        null=True,
    )

    def __str__(self):
        return self.title


class Question(models.Model):
    """Base questions to users."""

    text = models.CharField('Question', max_length=120)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Author',
        related_name='questions',
    )
    theme = models.ManyToManyField(
        to='Theme',
        related_name='questions',
        verbose_name='Themes',
    )

    def __str__(self):
        return self.text


class Hint(models.Model):
    """Additional questions.
    If user doesn't know what to say,
    these hints help to develop speech."""

    text = models.CharField('Hint', max_length=100)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='hints',
        verbose_name='Question',
    )

    def __str__(self):
        return self.text
