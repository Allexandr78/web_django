"""
Models for web_dj
"""
from django.db import models
from django.contrib.auth.models import User

TOPIC_TITLE = (
    ("S", "Sport"),
    ("C", "Cinema"),
    ("F", "Fashion")
)


class Topic(models.Model):
    """
    Модель темы, например: Спорт, Кино, Мода.
    """
    title = models.CharField(max_length=2, choices=TOPIC_TITLE)
    name = models.TextField(null=False, blank=False, max_length=20)
    subscribe = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """"
        Title name
        """
        return str(self.name)


class Article(models.Model):
    """
    Статья.
    """
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField('Topic', related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """"
        Title name
        """
        return str(self.title)


class Comment(models.Model):
    """
    Comment model
    """
    content = models.TextField(null=False, blank=False, )
    author = models.ForeignKey(User, on_delete=models.CASCADE, )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"
