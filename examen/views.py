from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'examen/home_sysqa.html', context)

def v1(request):
    context = {
        'posts': posts1
    }
    return render(request, 'examen/home_sysqa.html', context)

def v2(request):
    context = {
        'posts': posts2
    }
    return render(request, 'examen/home_sysqa.html', context)

def v3(request):
    return HttpResponse('<h1>Vraag 3</h1>')

def v4(request):
    return HttpResponse('<h1>Vraag 4</h1>')

def v5(request):
    return HttpResponse('<h1>Vraag 5</h1>')

def v6(request):
    return HttpResponse('<h1>Vraag 6</h1>')

def v7(request):
    return HttpResponse('<h1>Vraag 7</h1>')

def v8(request):
    return HttpResponse('<h1>Vraag 8</h1>')

def v9(request):
    return HttpResponse('<h1>Vraag 9</h1>')

def v10(request):
    return HttpResponse('<h1>Vraag 10</h1>')

def v11(request):
    return HttpResponse('<h1>Vraag 11</h1>')