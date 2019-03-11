from django.contrib import admin

# Register your models here.
from django.db import models
from .models import Article, Tag, ArticleTags
from martor.widgets import AdminMartorWidget


class TagsInlineAdmin(admin.StackedInline):
    model = Article.tags.through
    extra = 0 # 去除空行
    can_delete = True # 让文章关联的标签可以清除
class ArticleAdmin(admin.ModelAdmin):
    fielsets = [
        (None, {'fields': ['title', 'content', 'create_time', 'updata_time']})
    ]
    readonly_fields = ['create_time', 'updata_time'] # 只读模式 
    inlines = (TagsInlineAdmin,)
    
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)