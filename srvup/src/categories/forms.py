from django import forms

from .models import Category
from videos.models import Video


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
            'video',
        ]

    def __init__(self, *args, **kwargs):
        super(CategoryAdminForm, self).__init__(*args, **kwargs)
        obj = kwargs.get("instance")
        qs = Video.objects.all().unused()
        if obj:
            if obj.video:
                this_ = Video.objects.filter(pk=obj.video.pk)
                qs = (qs | this_)
        self.fields['video'].queryset = qs
