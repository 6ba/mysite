import datetime
from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField


from markdownx.models import MarkdownxField
from markdownx.widgets import AdminMarkdownxWidget
import datetime
from django.utils.encoding import python_2_unicode_compatible


# 栏目
@python_2_unicode_compatible
class LanMu(models.Model):
    lanmu = models.CharField('栏目', max_length=256)

    def __str__(self):
        return self.lanmu

    class Meta:
        verbose_name = '栏目'


# 标签 Tag ---BBS 放弃栏目 | 后期再根据 Tag名字 进行维护。
@python_2_unicode_compatible
class Tag(models.Model):
    # lanmu = models.ForeignKey(LanMu, blank=True, null=True, verbose_name='所属栏目')
    name = models.CharField('column_name', max_length=256,)
    intro = models.TextField('introduction', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = '标签'
        ordering = ['name']


@python_2_unicode_compatible
class Tie(models.Model):
    set_top = models.BooleanField('设为置顶', default=False)
    solved = models.BooleanField('是否结帖', default=False)
    wonderful = models.BooleanField('是精华', default=False)
    author = models.ForeignKey(User, null=True, related_name="author_set")
    tag = models.ForeignKey(Tag, blank=True, null=True, verbose_name='小标签')
    title = models.CharField(verbose_name="标题", max_length=256)
    # summary = models.TextField(verbose_name="概要", default=" ")
    content = UEditorField('内容', height=500, width=1200,
        default='', blank=True, imagePath="uploads/images/%(basename)s_%(datetime)s.%(extname)s",
        toolbars='full', filePath='uploads/files/%(basename)s_%(datetime)s.%(extname)s')
    pub_date = models.DateTimeField(verbose_name="发表时间", auto_now_add=True)
    see_num = models.IntegerField(verbose_name="浏览数", default=0)
    comment_num = models.IntegerField(verbose_name="评论", default=0)
    # published = models.BooleanField("发布与否", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ties'
        verbose_name_plural = '帖子'
        ordering = ['set_top', '-pub_date']


@python_2_unicode_compatible
class Comment(models.Model):
    puter = models.ForeignKey(User, null=True, related_name="user_set")
    tie = models.ForeignKey(Tie, null=True)
    content = MarkdownxField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    vote = models.IntegerField("点赞数", default=0)
    obj_id = models.IntegerField("回复给谁", default=0)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'


# 社区基本用户
@python_2_unicode_compatible
class WebUser(models.Model):
    phone = models.CharField("手机号", max_length=100)
    email = models.CharField("邮箱", max_length=100)
    password = models.CharField("密码", max_length=100)
    name = models.CharField("姓名", max_length=100)
    danwei = models.CharField("单位", max_length=100)
    zhiwu = models.CharField("职务", max_length=100)

    user_pic = models.ImageField(
        verbose_name='文章标头图片535*270',
        upload_to='uploads/user_pics/images/',
        default='uploads/images/defualt_user_pic.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "网站手机号注册用户"

