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
                'cover': article.cover.url,
                'created_at': article.created_at.date(),
                'category': article.category.title,
            })

        promote_data = []
        all_promote_articles = Article.objects.filter(promote=True)

        for promote_article in all_promote_articles:
            promote_data.append({
                'title': promote_article.title ,
                'cover': promote_article.cover.url if promote_article.cover else None,
                'created_at': promote_article.created_at.date(),
                'category': promote_article.category.title,
                'author': promote_article.author.user.first_name + ' ' + promote_article.author.user.last_name,
                'avatar': promote_article.author.avatar.url if promote_article.author.avatar else None,
            })

        context = {
            'article_data': article_data,
            'promote_article_data': promote_data,
        }

        return render(request=request, template_name='index.html', context=context)
    

class ContactPage(TemplateView):
    template_name = 'page-contact.html'
    