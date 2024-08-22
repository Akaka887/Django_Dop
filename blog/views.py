from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return render(request, 'blog/index.html')


def get_test(request):
    return HttpResponse('<h1>ТЕСТ</h1>')


def cats(request, number):
    if number == 404:
        raise Http404
    elif number == 1:
        return redirect('main', permanent=True)
    elif number == 2:
        return redirect('test')
    return HttpResponse(f'<h1>Число: {number}</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ошибка 404</h1>'
                                '<h2>Страница не найдена</h2>')

def info(request, name, age):
    return HttpResponse(f'<h1>Имя: {name}</h1>'
                        f'<h1>Возраст: {age}</h1>')