from django.contrib import admin

from .models import Phrase, PhraseTranslation, TranslationsStack


class PhraseTranslationInlines(admin.TabularInline):
    model = PhraseTranslation
    raw_id_fields = ('phrase',)
    extra = 1


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):

    list_filter = ('language_code',)
    search_fields = ('phrase',)

    class Meta:
        model = Phrase


@admin.register(TranslationsStack)
class TranslationsStackAdmin(admin.ModelAdmin):

    raw_id_fields = ('phrases',)
    search_fields = ('phrases',)
    list_filter = ('phrases__language_code',)
    inlines = [PhraseTranslationInlines]

    class Meta:
        model = TranslationsStack
