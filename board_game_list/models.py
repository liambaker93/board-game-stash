from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class BoardGameCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BoardGameList(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(BoardGameCategory, on_delete=models.CASCADE)
    description = models.TextField()
    image = CloudinaryField('image')
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_games")
    minplayers = models.IntegerField(default=1, validators=[MinValueValidator(1)], verbose_name="Mininmum Players:")
    maxplayers = models.IntegerField(default=1, validators=[MinValueValidator(1)], verbose_name="Maximum Players:")
    added_by = models.ManyToManyField(User, related_name="library_games", blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BoardGameList, self).save(*args, **kwargs)
    



