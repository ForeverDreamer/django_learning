from django.contrib import admin

from .models import Course, Lecture
from .forms import LectureAdminForm


class LectureInline(admin.TabularInline):
    model = Lecture
    form = LectureAdminForm
    prepopulated_fields = {"slug": ("title",)}
    # raw_id_fields = ['video']
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [LectureInline]
    list_filter = ['updated', 'timestamp']
    list_display = ['title', 'updated', 'timestamp']
    readonly_fields = ['updated', 'timestamp', 'short_title']
    search_fields = ['title', 'description']

    class Meta:
        model = Course

    def short_title(self, obj):
        return obj.title[:3]


admin.site.register(Course, CourseAdmin)
