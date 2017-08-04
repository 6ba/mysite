from django.conf.urls import url,include

#from bookreader.spyder import spyder
from bbs import views
from .auths_views import url_parterns


urlpatterns = [
    url(r'^$', views.index, name="bbs主页"),
    url(r'^write/$', views.put_tie, name="write_tie_for_user_self"),

    url(r'^ties/$', views.ties_index, name="帖子首页"),
    url(r'^solved/$', views.ties_solved, name="帖子解决"),
    url(r'^unsolved/$', views.ties_unsolved, name="帖子未结帖"),
    url(r'^wonderful/$', views.ties_wonderful, name="帖子精华"),

    url(r'^add/$', views.add, name="添加帖子"),

    url(r'^ties/(?P<tie_id>[0-9]+)/$', views.tie_detail, name="帖子详情页"),
    ## user_ 后台的 partern 让其他的写。
]

urlpatterns += url_parterns

# "HM6NR-QXX7C-DFW2Y-8B82K-WTYJV"