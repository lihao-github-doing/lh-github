import random
import string
# 111111
# 22222212122
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_protect

from user.captcha.image import ImageCaptcha
from user.models import TUser


def regist(request):
    return render(request,'user/register.html')
def register_logic(request):
    captcha = request.POST.get('captcha')
    if captcha.lower() == request.session.get('code').lower():
        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        res = TUser.objects.create(username=username,password=pwd,email=email)
        if res:
            request.session['is_login'] = True
            return HttpResponse('1')
        return HttpResponse('0')
    return HttpResponse('0')
def login(request):
    username = request.COOKIES.get('username')
    pwd = request.COOKIES.get('pwd')
    res = TUser.objects.filter(username=username, password=pwd)
    if res:
        request.session['is_login'] = True
        return redirect('usr:index')
    return render(request,'user/login.html')
def login_logic(request):

    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    res = TUser.objects.filter(username=username,password=pwd)
    if res:

        request.session['is_login'] = True
        return HttpResponse('1')
    return HttpResponse('0')


def index(request):
    is_login = request.session.get()
    if is_login:
        return render(request,'user/index.html')
    return redirect('usr:login')
# @csrf_protect
def check_username(request):
    username = request.POST.get('username')
    res = TUser.objects.filter(username=username)
    if res:
        return HttpResponse('用户名已存在')
    else:
        return HttpResponse('ok')


def get_captcha(request):
    image = ImageCaptcha()
    code = random.sample(string.ascii_letters+string.digits,4)
    code = ''.join(code)
    data = image.generate(code)
    print(code)
    request.session['code'] = code
    return HttpResponse(data,'image/png')
