from django.contrib import admin

from .models import Hint, Question, Theme


class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    class Meta:
        model = Theme

    inlines = (QuestionInLine,)


@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
    class Meta:
        model = Hint


class HintInLine(admin.TabularInline):
    model = Hint
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question

    inlines = (HintInLine,)
    list_display = ('text',)
    list_filter = ('theme',)
