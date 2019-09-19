from django.shortcuts import render


def index(request):
    return render(request=request, template_name='main/index.html', context={'foo': ['bar', 'baz']})
