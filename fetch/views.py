from django.shortcuts import render


def hello(request):
    from fetch import settings
    print(settings.STATICFILES_DIRS)
    return render(request, 'hello.html', {})
