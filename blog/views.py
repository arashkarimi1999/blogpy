from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class IndexPage(TemplateView):
    
    def get(self, request, **kwargs):

        article_data = []
        all_article = Article.objects.all().order_by('-created_at')[:8]

        for article in all_article:
            article_data.append({
                'title': article.title ,
                'cover' : article.cover.url,
                'created_at' : article.created_at.date(),
                'category' : article.category.title,
            })

        context = {
            'article_data' : article_data,
        }

        return render(request=request, template_name='index.html', context=context)