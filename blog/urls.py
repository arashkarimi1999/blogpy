from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('article/', views.SingleArticleAPIView.as_view(), name='single_article'),
    path('article/all/', views.AllArticleAPIView.as_view(), name='all_articles'),
    path('article/search/', views.SearchArticleAPIView.as_view(), name='search_article'),
    path('article/submit/', views.SubmitArticleAPIView.as_view(), name='submit_article'),
    path('article/update_cover', views.UpdateARticleAPIView.as_view(), name='update_article'),
]