from django.conf.urls import url,include

#from bookreader.spyder import spyder
from bbs import views

urlpatterns = [
    url(r'^$', views.index, name="bbs主页"),

]

# "HM6NR-QXX7C-DFW2Y-8B82K-WTYJV"