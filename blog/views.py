from django.shortcuts import render
from django.http import HttpResponse


def posts_list(request):
    name = 'Mane'
    return render(request, 'blog/base.html', context={
        'name': name
    })
