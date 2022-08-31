# coding-utf-8
from django.http.response import HttpResponse


def index_view(request):
    return HttpResponse('hello world 2')
