"""
URL Configuration
"""
from django.urls import path

from web_dj.views import home, my_feed, article_detail, add_comment, article_upd, article_del, article_create, topics, \
    topic_subscribe, topic_unsubscribe, profile, register, set_password, login_user, logout_user, articles_by_date

urlpatterns = {
    path('', home, name='index'),
    path('my-feed/', my_feed, name='my-feed'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('<int:article_id>/coment/', add_comment, name='add_comment'),
    path('<int:article_id>/update/', article_upd, name='article_upd'),
    path('<int:article_id>/delete/', article_del, name='article_del'),
    path('create/', article_create, name='article_create'),
    path('topics/', topics, name='topics'),
    path('topics/<int:topic_id>/', topic_subscribe, name='topic_subscribe'),
    path('topics/<int:topic_id>/subscribe/', topic_subscribe, name='topic_subscribe'),
    path('topics/<int:topic_id>/unsubscribe/', topic_unsubscribe, name='topic_unsubscribe'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('set-password/', set_password, name='set_password'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('<int:year>/<int:month>/', articles_by_date, name='articles_by_date'),
}
