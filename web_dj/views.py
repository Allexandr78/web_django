"""
Модуль предназначен для реализации основных функций обработки данных.

"""
import datetime

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, request
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Article
from .models import Topic


def home(request: HttpRequest) -> HttpResponse:
    """ Основная страница, на которой будет список всех статей."""

    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'articles': articles})


def my_feed(request: HttpRequest) -> HttpResponse:
    """Страница, на которой будут только статьи по темам, на которые подписан пользователь."""
    topic_ids = Topic.objects.filter(subscribe=request.user).values_list('name', flat=True)
    article = Article.objects.filter(subscribers__name__in=topic_ids).values_list('title', flat=True)

    return render(request, 'my_feed.html', {'topics_ids': topic_ids, 'articles': article})


def article_detail(request: HttpRequest, article_id: int) -> HttpResponse:
    """Страница, на которой будет отображаться статья по id."""
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})


def add_comment(request: HttpRequest, article_id: int) -> HttpResponse:
    """Адрес, который мы будем использовать для написания комментариев к статье #"""
    return HttpResponse(
        f"Адрес, который мы будем использовать для написания комментариев к статье # {article_id}.")


def article_upd(request: HttpRequest, article_id: int) -> HttpResponse:
    """Страница, которую мы будем использовать для изменения существующей статьи #"""
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_upd.html', {'article_id': article_id, 'article': article})


def article_del(request: HttpRequest, article_id: int) -> HttpResponse:
    """Адрес, который мы будем использовать для удаления статьи #"""
    return HttpResponse(
        f"Адрес, который мы будем использовать для удаления статьи #{article_id} .")


def article_create(request: HttpRequest) -> HttpResponse:
    """Страница, на которой мы будем создавать новые статьи."""
    return render(request, 'article_create.html')


def topics(request: HttpRequest) -> HttpResponse:
    """Страница, с перечнем всех тем на сайте."""
    topic_titles = Topic.objects.all().values_list('name', flat=True)
    return render(request, 'topics.html', {'topics': topic_titles})


def topic_articles(request: HttpRequest, topic_id: int) -> HttpResponse:
    """Страница, со всеми статьями по определенной теме #"""
    return render(request, 'topic_articles.html', {'topic_id': topic_id})


def topic_subscribe(request: HttpRequest, topic_id: int) -> HttpResponse:
    """Адрес для подписки на конкретную тему #"""
    return HttpResponse(f"Адрес для подписки на конкретную тему # {topic_id}.")


def topic_unsubscribe(request: HttpRequest, topic_id: int) -> HttpResponse:
    """Адрес для отписки от конкретной темы #"""
    return HttpResponse(f"Адрес для отписки от конкретной темы #{topic_id} .")


def profile(request: HttpRequest) -> HttpResponse:
    """Страница, с данными пользователя и перечнем его подписок."""
    return render(request, 'profile.html')


def register(request: HttpRequest) -> HttpResponse:
    """Страница, регистрацией нового пользователя."""
    return render(request, 'register.html')


def set_password(request: HttpRequest) -> HttpResponse:
    """Страница, с изменением пароля."""
    return render(request, 'set_password.html')


def login_user(request: HttpRequest) -> HttpResponse:
    """Страница, для входа на сайт."""
    return render(request, 'login_user.html')


def logout_user(request: HttpRequest) -> HttpResponse:
    """Адрес для выхода с сайта."""
    return HttpResponse(" Адрес для выхода с сайта.")


def articles_by_date(request: HttpRequest, year: int, month: int) -> HttpResponse:
    """Страница, на которой будут статьи созданные в конкретный месяц {month} {year}.
    В случае запроса не настоящей даты, должна быть ошибка."""
    try:
        datetime.date(year, month, 1)
        articles_date = Article.objects.filter(created_at__year=year, created_at__month=month)
        return render(request, 'articles_by_date.html', {'year': year, 'month': month, 'articles': articles_date})
    except ValueError:
        return HttpResponseNotFound("В случае запроса не настоящей даты, должна быть ошибка.")
