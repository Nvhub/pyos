from django.contrib import admin
from .models import Article, Category, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user_name', 'created_at']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
