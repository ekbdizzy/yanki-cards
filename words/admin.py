from django.contrib import admin

from .models import Phrase, UserPhrase


class UserPhraseInLine(admin.TabularInline):
    model = UserPhrase
    raw_id_fields = ('user',)
    extra = 1


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    class Meta:
        model = Phrase

    raw_id_fields = ('users',)
    list_filter = ('language',)
    inlines = (UserPhraseInLine,)
