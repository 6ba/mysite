from django.shortcuts import render

from .models import Tie, Comment
## 用户管理的后台 所有的view. urls, 全部写在这里

def user_index(request):
    return render(request, "bbs/users/user_index.html")


def user_set(request):
    return render(request, "bbs/users/user_set.html")


def user_home(request):
    user = request.user
    own_ties = Tie.objects.filter(author=user)
    own_comments = Comment.objects.filter(puter=user)
    return render(request, "bbs/users/user_home.html", {

        "own_ties": own_ties,
        "own_comments": own_comments,
    })


def user_ties(request):

    return render(request, "bbs/users/user_set.html", )

def user_msg(request):

    return render(request, "bbs/users/user_msg.html", )

# 邮箱激活
def user_active(request):

    return render(request, "bbs/users/user_active.html", )


## URLS
from django.conf.urls import url


url_parterns = [

    url(r'^user/$', user_index, name="user_center"),
    url(r'^user_home/$',user_home, name="user_home"),
    url(r'^user/set/$', user_set, name="user_set"),
    url(r'^user/ties/$', user_ties, name="user_ties"),

    url(r'^user/massage/$', user_msg, name="user_msg"),
    url(r'^user/active/$', user_active, name="user_msg"),
]