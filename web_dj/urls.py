"""
URL Configuration
"""

from django.urls import path

from web_dj import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-feed/', views.my_feed, name='my-feed'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/coment/', views.add_comment, name='add_comment'),
    path('<int:article_id>/update/', views.article_upd, name='article_upd'),
    path('<int:article_id>/delete/', views.article_del, name='article_del'),
    path('create/', views.article_create, name='article_create'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic_articles, name='topic_articles'),
    path('topics/<int:topic_id>/', views.topic_subscribe, name='topic_subscribe'),
    path('topics/<int:topic_id>/subscribe/', views.topic_subscribe, name='topic_subscribe'),
    path('topics/<int:topic_id>/unsubscribe/', views.topic_unsubscribe, name='topic_unsubscribe'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('set-password/', views.set_password, name='set_password'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('<int:year>/<int:month>/', views.articles_by_date, name='articles_by_date'),
]
