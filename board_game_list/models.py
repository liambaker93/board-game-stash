from django.db import models

# Create your models here.


class BoardGameCategory(models.Model):
    name = models.CharField(max_length=200)


class BoardGameList(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(BoardGameCategory, on_delete=models.CASCADE)
    description = models.CharField()



