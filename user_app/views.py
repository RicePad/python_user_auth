from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'user_app/index.html')


def register(request):
    pass


def user_login(request):
    pass
