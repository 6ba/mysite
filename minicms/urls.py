from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from bookreader.spyder import spyder
# from bbs import views
from blog import views


urlpatterns = [
    url(r'^$', views.index, name="主页"),
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
	url(r'^blog/', include('blog.urls')),
    # url(r'^weixin/', include('weixin.urls')),
    url(r'^bbs/', include('bbs.urls')),
    # denglu/zhuce/accout
    ##set more
    #url(r'^test1/', spyder.test),
    url(r'^t/', include('test_app.urls')),
]

from bbs.acounts import url_patterns
urlpatterns.extend(url_patterns)

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)



