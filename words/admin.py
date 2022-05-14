from django.contrib import admin

from .models import Phrase, PhraseTranslation, TranslationsStack


class PhraseTranslationInlines(admin.TabularInline):
    model = PhraseTranslation
    raw_id_fields = ('phrase',)
    extra = 1


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    class Meta:
        model = Phrase

    list_filter = ('language',)
    search_fields = ('phrase',)


@admin.register(TranslationsStack)
class TranslationsStackAdmin(admin.ModelAdmin):
    class Meta:
        model = TranslationsStack

    raw_id_fields = ('phrases',)
    search_fields = ('phrases',)
    inlines = [PhraseTranslationInlines]
