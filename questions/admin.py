from django.contrib import admin

from .models import Hint, Question, Theme


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    class Meta:
        model = Theme


@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
    class Meta:
        model = Hint


class HintInLine(admin.TabularInline):
    model = Hint
    # raw_id_fields = ('text',)
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question

    inlines = (HintInLine,)
    list_display = ('text',)
    list_filter = ('theme',)
    raw_id_fields = ('author',)
