from django.urls import path
from .view.category import *
from .view import article, comment


app_name = 'admin-panel'



# CATEGORY
urlpatterns = [
    path('category/', index, name='category-index'),
    path('category/show/<int:id>', show, name='category-show'),
    path('category/delete/<int:id>', delete, name='category-delete'),
    path('category/create', create, name='category-create'),
    path('category/update/<int:id>', update, name='category-update'),

]

# ARTICLE

urlpatterns += [
    path('article/', article.index, name='article-index'),
    path('article/show/<int:id>', article.show, name='article-show'),
    path('article/create/', article.create.as_view(), name='article-create'),
    path('article/delete/<int:id>', article.delete, name='article-delete'),
    path('article/update/<int:pk>', article.update.as_view(), name='article-update')

]

# COMMENT

urlpatterns += [
    path('comment/', comment.index, name='comment-index'),
    path('comment/show/<int:id>/', comment.show, name='comment-show'),
    path('comment/status/<int:id>/', comment.status, name='comment-status'),
    path('comment/delete/<int:id>/', comment.delete, name='comment-delete')
]