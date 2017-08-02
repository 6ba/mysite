from django.shortcuts import render


## 用户管理的后台 所有的view. urls, 全部写在这里

def user_index(request):
    return render(request, "bbs/user/user_index.html")


def user_set(request):
    return render(request, "bbs/user/user_set.html")