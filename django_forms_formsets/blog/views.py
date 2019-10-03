from django.shortcuts import render
from django.utils import timezone

from .forms import TestForm, PostModelForm


def home(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.title = 'Some random title'
        obj.publish = timezone.now()
        obj.save()
    if form.has_error:
        print('as_json: ', form.errors.as_json())
        print('as_text: ', form.errors.as_text())
        # print(dir(form.errors))
        data = form.errors.items()
        for key, value in data:
            # print(dir(value))
            error_str = '{field}: {error}'.format(
                field=key,
                error=value.as_text()
            )
            print(error_str)
        print('non_field_errors: ', form.non_field_errors())
    # initial_dict = {
    #     # 'some_text': 'Text',
    #     'boolean': True,
    #     # 'integer': 123
    # }
    # form = TestForm(request.POST or None, initial=initial_dict)
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     print(form.cleaned_data.get('some_text'))
    #     print(form.cleaned_data.get('email'))
    #     print(form.cleaned_data.get('email2'))

    # if request.method == 'POST':
    #     form = TestForm(data=request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         print(form.cleaned_data.get('some_text'))
    #     print(request.POST)
    #     print(request.POST.get('username'))  # None
    #     print(request.POST['username2'])  # Raise Error
    # elif request.method == 'GET':
    #     # form = TestForm(user=request.user)
    #     form = TestForm()
    #     print(request.GET)
    return render(request, 'forms.html', {'form': form})
