from django.forms import ModelForm
from ..models import Category, Article


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleForm(ModelForm):

      class Meta:
        model = Article
        fields = '__all__'
