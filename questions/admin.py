from django.contrib import admin

from .models import Hint, Question, Theme


class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):

    inlines = (QuestionInLine,)

    class Meta:
        model = Theme


@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
    class Meta:
        model = Hint


class HintInLine(admin.TabularInline):
    model = Hint
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    inlines = (HintInLine,)
    list_display = ('text',)
    list_filter = ('theme',)

    class Meta:
        model = Question
