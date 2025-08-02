from django.shortcuts import render
from django.views import generic
from .models import BoardGameList
# Create your views here.


class PostList(generic.ListView):
    queryset = BoardGameList.objects.filter()
    template_name = "list/library.html"
    
