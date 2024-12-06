"""
Модуль предназначен для реализации основных функций обработки данных.

Описание:
- В этом модуле реализованы функции для чтения, обработки и вывода данных.
- Модуль нацелен на обработку текстовых файлов и может быть расширен для работы с другими форматами.

Функции:
- read_data(filepath): функция для чтения данных из файла.
- process_data(data): функция для обработки данных.
- output_data(processed_data): функция для вывода обработанных данных.

Дата создания: 01.12.2024
Версия: 1.0
"""
import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound


def home(request: HttpRequest) -> HttpResponse:
    """ Основная страница, на которой будет список всех статей."""
    return render(request, 'home.html')


def my_feed(request: HttpRequest) -> HttpResponse:
    """Страница, на которой будут только статьи по темам, на которые подписан пользователь."""
    return render(request, 'my_feed.html')


def article_detail(request: HttpRequest, article_id: int) -> HttpResponse:
    """Страница, на которой будет отображаться статья по id."""
    if article_id:
        return render(request, 'article_detail.html', {'article_id': article_id})
    else:
        return HttpResponseNotFound("Статья не найдена.")



def add_comment(request: HttpRequest, article_id: int) -> HttpResponse:
    """Адрес, который мы будем использовать для написания комментариев к статье #"""
    return HttpResponse(
        f"Адрес, который мы будем использовать для написания комментариев к статье # {article_id}.")


def article_upd(request: HttpRequest, article_id: int) -> HttpResponse:
    """Страница, которую мы будем использовать для изменения существующей статьи #"""
    return render(request, 'article_upd.html', {'article_id': article_id})


def article_del(request: HttpRequest, article_id: int) -> HttpResponse:
    """Адрес, который мы будем использовать для удаления статьи #"""
    return HttpResponse(
        f"Адрес, который мы будем использовать для удаления статьи #{article_id} .")


def article_create(request: HttpRequest) -> HttpResponse:
    """Страница, на которой мы будем создавать новые статьи."""
    return render(request, 'my_feed.html')


def topics(request: HttpRequest) -> HttpResponse:
    """Страница, с перечнем всех тем на сайте."""
    return render(request, 'topics.html')


def topic_articles(request: HttpRequest, topic_id: int) -> HttpResponse:
    """Страница, со всеми статьями по определенной теме #"""
    return render(request, 'article_upd.html', {'topic_id': topic_id})


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
        return render(request, 'article_upd.html', {'year': year, 'month': month})
    except ValueError:
        return HttpResponseNotFound("В случае запроса не настоящей даты, должна быть ошибка.")
