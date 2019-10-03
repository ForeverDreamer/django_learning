from django import forms

from .models import Post


class PostModelForm(forms.ModelForm):
    # Don't do this
    # title = forms.CharField(
    #     max_length=120,
    #     label='Some field',
    #     help_text='some help text',
    #     error_messages={
    #         'required': 'The title field is required.'
    #     }
    # )
    class Meta:
        model = Post
        fields = ['user', 'title', 'slug', 'image']
        # exclude = ['height_field', 'width_field']
        labels = {
            'title': 'this is title label',
            'slug': 'This is slug'
        }
        help_texts = {
            'title': '这是标签',
            'slug': '这是slug'
        }
        # error_messages = {
        #     'title': {
        #         'max_length': 'This title is too long.',
        #         'required': 'The title field is required.'
        #     },
        #     'slug': {
        #         'max_length': 'This title is too long.',
        #         'required': 'The title field is required.',
        #         'unique': 'The slug field must be unique.'
        #     },
        # }

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.Textarea()
        self.fields['title'].error_messages = {
            'max_length': 'This title is too long.',
            'required': 'The title field is required.'
        }
        self.fields['slug'].error_messages = {
            'max_length': 'This title is too long.',
            'required': 'The title field is required.',
            'unique': 'The slug field must be unique.'
        }

        for field in self.fields.values():
            field.error_messages = {
                'required': 'You know, {fieldname} is required'.format(fieldname=field.label)
            }

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')
    #     return title

    # def save(self, commit=True, *args, **kwargs):
    #     obj = super(PostModelForm, self). save(commit=False, *args, **kwargs)
    #     obj.publish = '2016-10-01'
    #     obj.content = 'Coming soon'
    #     if commit:
    #         obj.save()
    #     return obj


SOME_CHOICES = {
    ('db-value1', 'display Value1'),
    ('db-value2', 'display Value2'),
    ('db-value3', 'display Value3'),
}

INTS_CHOICES = [tuple([x, x]) for x in range(0, 100)]

YEARS = [x for x in range(1980, 2031)]


class TestForm(forms.Form):
    date_field = forms.DateField(initial='2010-01-20', widget=forms.SelectDateWidget(years=YEARS))
    some_text = forms.CharField(label='Text', widget=forms.Textarea(attrs={'row': 4, 'cols': 10}))
    choices = forms.CharField(label='Text', widget=forms.CheckboxSelectMultiple(choices=SOME_CHOICES))
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=10, widget=forms.Select(choices=INTS_CHOICES))
    email = forms.EmailField(min_length=10)

    def __init__(self, user=None, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['some_text'].initial = user.username

    def clean_integer(self, *args, **kwargs):
        integer = self.cleaned_data.get('integer')
        if integer < 10:
            raise forms.ValidationError('The integer must be greater than 10')
        return integer

    def clean_some_textr(self, *args, **kwargs):
        some_text = self.cleaned_data.get('some_text')
        if len(some_text) < 10:
            raise forms.ValidationError('Ensure the text is greater than 10 characters')
        return some_text
