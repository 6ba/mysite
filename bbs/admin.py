from django.contrib import admin

# Register your models here.
from .models import LanMu, Tag, Tie, Comment

## 注册到后台只是为了测试的时候方便检查, 后期关掉。

admin.site.register(LanMu)
admin.site.register(Tie)
admin.site.register(Comment)
admin.site.register(Tag)

