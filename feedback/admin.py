from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    class Meta:
        model = Feedback

    list_display = ("theme", "title", "status", "user", "created_at")
    list_filter = ('status', 'theme')
    search_fields = ('user',)
    raw_id_fields = ('user',)
    readonly_fields = ("created_at",)
    ordering = ('created_at',)
