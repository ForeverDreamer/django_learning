from django.contrib import admin

from .models import Course, Lecture, MyCourses
from .forms import LectureAdminForm

admin.site.register(MyCourses)


class LectureInline(admin.TabularInline):
    model = Lecture
    form = LectureAdminForm
    prepopulated_fields = {"slug": ("title",)}
    # raw_id_fields = ['video']
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [LectureInline]
    list_filter = ['updated', 'timestamp']
    list_display = ['title', 'category', 'updated', 'timestamp']
    readonly_fields = ['updated', 'timestamp', 'short_title']
    search_fields = ['title', 'description']
    list_editable = ['category']

    class Meta:
        model = Course

    def short_title(self, obj):
        return obj.title[:3]


admin.site.register(Course, CourseAdmin)
