from django.shortcuts import render
from django.http import HttpResponse


def posts_list(request):
    names = ['Mane', 'Egor', 'Katya']
    return render(request, 'blog/index.html', context={
        'names': names
    })
