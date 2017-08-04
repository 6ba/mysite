import re
import time

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.timezone import now

from .models import WebUser
from .forms import LoginForm, RegisterForm


# 姓名、手机号码、单位、职务、邮箱 ^1(3|4|5|7|8)\d{9}$
def my_authenticate(username, password):
    try:
        user = User.objects.get(username=username)
        print(WebUser.objects.get(phone=username).password)
        if password == user.password:
            # print("密码符合")
            return True
        return False
    except:
        # print("抛出用户错误！！" + username + ", " + password)
        return False


def homepage(request):
    return log_in(request)


def log_in(request):

    if request.method == 'GET':

        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        try:
            if request.GET["next"]:
                request.session['login_from'] = request.GET["next"]
        except:
            pass

        form = LoginForm()
        # request.session['login_from'] = request.META.get('HTTP_REFERER', '/wxb1/')
        return render(request, 'accounts/login.html', {'form': form})

    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['uid']
            password = form.cleaned_data['pwd']

            if not username in [x.username for x in User.objects.all()]:
                return render(request, 'accounts/login.html', {'form': form, 'error': "账号不存在！"})
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                user.last_login = now()
                print("jinxingugo"+ request.session['login_from'])
                return redirect(request.session['login_from'])
            else:
                # 失败了也要进——用自己的认证
                if my_authenticate(username, password):
                    try:
                        time.sleep(3)
                        user = User.objects.get(username=username)
                        user.last_login = now()
                        login(request, user)
                        return redirect(request.session['login_from'])
                    except:
                        pass
                return render(request, 'accounts/login.html', {'form': form, 'error': "密码错误！"})
        else:
            return render(request, 'accounts/login.html', {'form': form})


@login_required
def log_out(request):
    if request.method == 'GET':
        request.session['logout_from'] = request.META.get('HTTP_REFERER', '/')
        url = request.POST.get('source_url', '/')
        logout(request)
    try:
        return redirect(request.session['logout_from'])
    except:
        return redirect(url)

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'auths/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():

            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            name = form.cleaned_data['name']
            danwei = form.cleaned_data['danwei']
            zhiwu = form.cleaned_data['zhiwu']

            # ^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$
            if not re.match("^1(3|4|5|7|8)\d{9}$", phone):
                return render(request, 'auths/register.html', {'form': form, 'msg': "手机号不符合规范"})

            if not re.match("^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email):
                return render(request, 'auths/register.html', {'form': form, 'msg': "邮箱不符合规范"})

            if password1 != password2:
                return render(request, 'auths/register.html', {'form': form, 'msg': "两次密码不一致"})

            if phone in [x.username for x in User.objects.all()]:
                return render(request, 'auths/register.html', {'form': form, 'msg': "该账号已存在"})

            WebUser.objects.create(phone=phone, password=password1, email=email, danwei=danwei, name=name, zhiwu=zhiwu)
            user = User.objects.create(username=phone, password=password1, email=email)
            user.last_login = now()
            user.has_perm("session.add_session")
            user.has_perm("session.change_session")
            user.has_perm("session.delete_session")
            login(request, user)

            return render(request, 'auths/register.html', {'form': form, 'flag': True})

        else:
            return render(request, 'auths/register.html', {'form': form})


def refind_pw(request):
    return HttpResponse("Not Find")



from .acounts import log_in, log_out, register
from django.conf.urls import url


url_patterns = [
    url(r'^accounts/login/$', log_in, name="bbs主页"),
    url(r'^accounts/logout/$', log_out, name="write_tie_for_user_self"),
    url(r'^accounts/register/$', register, name="write_tie_for_user_self"),
]

