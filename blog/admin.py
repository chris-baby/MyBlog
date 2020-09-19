from django.contrib import admin
from .models import Article,Category

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'img',
        'content',
        'abstract',
        'visited',
        'created_time',
        'updated_time'

    ]
    search_fields = list_display
    list_filter = list_display


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = list_display
    list_filter = list_display

# admin.site.register(Article)
# admin.site.register(Category)

