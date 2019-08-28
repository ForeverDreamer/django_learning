from django.contrib import admin

from .models import Category
from .forms import CategoryAdminForm


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['timestamp', 'updated']
    list_display = ['title', 'timestamp', 'updated']
    readonly_fields = ['timestamp', 'updated', 'short_title']
    search_fields = ['title']
    form = CategoryAdminForm

    class Meta:
        model = Category

    def short_title(self, obj):
        return obj.title[:3]


admin.site.register(Category, CategoryAdmin)
