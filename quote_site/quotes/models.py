from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    born_location = models.CharField(max_length=150)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)

class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    def __str__(self):
        return self.text