from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class BoardGameCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BoardGameList(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(BoardGameCategory, on_delete=models.CASCADE)
    description = models.CharField()
    image = models.ImageField(default='none')
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.title
    



