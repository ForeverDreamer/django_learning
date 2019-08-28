from django.contrib import admin

from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_filter = ['timestamp', 'updated']
    list_display = ['title', 'timestamp', 'updated']
    readonly_fields = ['timestamp', 'updated', 'short_title']
    search_fields = ['title', 'embed_code']

    class Meta:
        model = Video

    def short_title(self, obj):
        return obj.title[:3]


admin.site.register(Video, VideoAdmin)
