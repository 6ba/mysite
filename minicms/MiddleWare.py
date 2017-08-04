from django.shortcuts import render, redirect
import re


try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x
 
 
# 登陆验证中间件
class LoginMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):

        temp_url = request.META["PATH_INFO"]
        print(temp_url)
        if re.match(".*?/user.*?", temp_url):
            if not request.user.is_authenticated():
                return redirect("/accounts/login/")

        return view_func(request, *view_args, **view_kwargs)

'''
    def process_response(self, request, view_func):
        temp_url = request.META.get('HTTP_REFERER', '/wxb1/')
        print(temp_url)
        if re.match(".*?/wxb1/.*?", temp_url):
            if not request.user.is_authenticated():
                return redirect("/auths/login/")

        return view_func(self, request, view_func)
'''