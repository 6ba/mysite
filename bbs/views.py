from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tie, Tag, Comment


def index(request):

    last_top_comments_ties = [Tie.objects.all()[0] for i in range(9)]
    last_hots_ties = [Tie.objects.all()[3] for i in range(9)]
    top_users = [request.user for i in range(12)]
    top_ties = [Tie.objects.filter(set_top=True)][:2]
    ties = [Tie.objects.all()[1] for i in range(9)]

    return render(request, "bbs/homepage.html", {
        "ties": ties,
        "last_top_comments_ties": last_top_comments_ties,
        "last_hots_ties": last_hots_ties,
        "top_users": top_users,
        "top_ties": top_ties,
    })


# 写入
@login_required
def put_tie(request):
    user = request.user

    if request.method == 'GET':
        return render(request, "bbs/post_tie.html", {})

    if request.method == 'POST':

        tag = request.POST["tag"]
        title=request.POST["title"]
        content=request.POST["content"]
        if not tag in [t.name for t in Tag.objects.all()]:
            Tag.objects.create(name=tag, )

        _tag = Tag.objects.get(name=tag)
        Tie.objects.create(
            title=title,
            content=content,
            author=user,
            tag=_tag,
        )

        return HttpResponse("写入完成")

    return render(request, "bbs/post_tie.html", {

        })


def ties_index(request):
    tie = Tie.objects.get(id=3)
    ties = [tie for i in range(12)]
    return render(request, "bbs/tie.html", {
        "ties":ties,
    })


def ties_solved(request):
    tie = Tie.objects.get(id=3)
    ties = [tie for i in range(12)]
    return render(request, "bbs/tie.html", {
        "ties":ties,
    })



def ties_unsolved(request):
    tie = Tie.objects.get(id=2)
    ties = [tie for i in range(12)]
    return render(request, "bbs/tie.html", {
        "ties": ties,
    })


def ties_wonderful(request):
    tie = Tie.objects.get(id=1)
    ties = [tie for i in range(12)]
    return render(request, "bbs/tie.html", {
        "ties": ties,
    })


def tie_detail(request, tie_id):

    tie_id = int(tie_id)
    tie = Tie.objects.get(id=tie_id)

    if request.method == 'GET':
        try:
            comments = Comment.objects.filter(tie=tie)
        except:
            comments = None
        # comments = Comment.objects.all()
        # 评论排行 8个, 浏览排行 8 个
        comment_top_ties = [Tie.objects.get(id=2) for i in range(8)]
        seen_top_ties = [Tie.objects.get(id=3) for i in range(8)]

        return render(request, "bbs/tie_detail.html", {

            "tie": tie,
            "seen_top_ties": seen_top_ties,
            "comment_top_ties": comment_top_ties,
            "comments": comments,
        })

    # 提交评论了
    if request.method == 'POST':
        if not request.user.is_authenticated():
            return redirect("/accounts/login/")
        # 登陆状态下才能提交
        Comment.objects.create(
            puter=request.user,
            tie=tie,
            content=request.POST["content"],
        )
        return redirect("/bbs/ties/"+ str(tie_id) +"/")


# 写入
@login_required
def add(request):
    user = request.user

    if request.method == 'GET':
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        try:
            if request.GET["next"]:
                request.session['login_from'] = request.GET["next"]
        except:
            pass

        return render(request, "bbs/add.html", {})

    if request.method == 'POST':

        tag = request.POST["cate"]
        title = request.POST["title"]
        content = request.POST["content"]
        vercode = request.POST["vercode"]
        if not tag in [t.name for t in Tag.objects.all()]:
            Tag.objects.create(name=tag, )

        _tag = Tag.objects.get(name=tag)
        Tie.objects.create(
            title=title,
            content=content,
            author=user,
            tag=_tag,
        )
        # 可以设置一个中间页面的模板; 进行渲染跳转。
        # return HttpResponse("写入完成")
        return redirect(request.session['login_from'])

    return render(request, "bbs/add.html", {

        })