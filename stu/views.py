from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 渲染登录页面


def index_view(request):
    return render(request, 'login.html')

# 处理登录


def login_view(request):
    # 接受请求参数
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    # 判断
    if username == 'zhangsan' and password == '123':
        return HttpResponse('login successfully!')

    return HttpResponse('failed to login.')
