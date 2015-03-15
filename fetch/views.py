from django.shortcuts import render


def hello(request):
    return render(request, 'hello.html', {})


def dashboard(request):
    return render(request, 'dashboard.html', {})
