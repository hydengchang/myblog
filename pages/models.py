from django.db import models

# Create your models here.
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    content = models.TextField(max_length=500, verbose_name="内容")
    create_time = models.DateTimeField("创建时间", default=timezone.now)
    updata_time = models.DateTimeField("最新修改时间", auto_now=True)
    tags = models.ManyToManyField('Tag', through='ArticleTags')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        app_label = 'pages'


class Tag(models.Model):

    name = models.CharField(max_length=20, verbose_name="标签名")
    articles = models.ManyToManyField('Article', through='ArticleTags')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
        app_label = 'pages'


class ArticleTags(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)

    def __str__(self):
        return '{0}[{1}]'.format(self.article.title, self.tag.name)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = '文章标签'
        app_label = 'pages'