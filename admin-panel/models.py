from django.db import models
from django.utils import timezone
from account.models import User


class Category(models.Model):
    STATUS_CHOICES = (
        ['e', 'enable'],
        ['d', 'disable']
    )

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Article(models.Model):

    STATUS_CHOICES = [
        ('e', 'enable'),
        ('d', 'disable')
    ]

    title = models.CharField(max_length=80)
    body = models.TextField()
    status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def category_show(self):
        return ', '.join([category.name for category in self.category.all()])


class Comment(models.Model):

    STATUS_CHOICES = [
        ('e', 'enable'),
        ('d', 'disable')
    ]

    text = models.CharField(max_length=500)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='e')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
