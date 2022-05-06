from django.contrib import admin

from .models import UserWord, Word


class UserWordInLine(admin.TabularInline):
    model = UserWord
    raw_id_fields = ('user',)
    extra = 1


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    class Meta:
        model = Word

    raw_id_fields = ('users',)
    list_filter = ('language',)
    inlines = (UserWordInLine,)
