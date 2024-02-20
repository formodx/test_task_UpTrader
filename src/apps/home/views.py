from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def solve(request, text):
    return render(request, 'home/solve.html', {'text': text})