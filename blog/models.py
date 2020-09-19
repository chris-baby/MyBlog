import uuid, os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse, reverse_lazy

# from markdownx.models import MarkdownxField
# from markdownx.utils import markdownify
# from taggit.managers import TaggableManager
#
# from django.utils.functional import cached_property


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='类别名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    # class Tag(models.Model):
    #     name = models.CharField(max_length=255,verbose_name='标签')

    #     def __str__(self):
    #         return self.name

    # class Meta:
    #     verbose_name = '博客标签'
    #
    #     verbose_name_plural = verbose_name


def article_img_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
    # return '{0}/{1}/{2}'.format(instance.user.id,"avatar",filename)
    return os.path.join('avatar', filename)


class Article(models.Model):
    title = models.CharField(verbose_name="文章标题", max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者", related_name="articles")
    img = models.ImageField(upload_to=article_img_path, null=True, blank=True, verbose_name="文章配图")
    content = models.TextField(verbose_name="文章内容")
    # content = MarkdownxField(verbose_name="内容")
    abstract = models.TextField(verbose_name="文章摘要",null=True,blank=True,max_length=255)
    # abstract = MarkdownxField(verbose_name="文章摘要", null=True, blank=True, max_length=255)
    visited = models.PositiveIntegerField(verbose_name="访问量", default=0)
    category = models.ManyToManyField(Category, verbose_name="文章分类")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "文章内容"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    # 可以通过调用这个函数，直接返回详情页的url地址
    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"a_id": self.id})

    # reverse适合FBV
    # reverse_lay 适用于 CBV

    # 访问量加1
    def increase_visited(self):
        self.visited += 1
        self.save(update_fields=['visited'])

    # # 讲markdown转化成html
    # def get_markdown(self):
    #     return markdownify(self.content)


class SendEmail(models.Model):
    name = models.CharField(max_length=20, verbose_name='用户名')
    title = models.CharField(max_length=20, verbose_name='邮件标题')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    content = models.CharField(max_length=255, verbose_name='邮件内容')
    send_time = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '发送邮箱'
        verbose_name_plural = verbose_name


