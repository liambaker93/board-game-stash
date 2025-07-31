from django.contrib import admin
from .models import BoardGameCategory, BoardGameList

# Register your models here.
admin.site.register(BoardGameList)
admin.site.register(BoardGameCategory)
