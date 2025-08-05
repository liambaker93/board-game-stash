from django.shortcuts import render, redirect
from django.views import generic
from .models import BoardGameList
from .forms import LibraryUpdateForm
# Create your views here.


class PostList(generic.ListView):
    print("these are the library games")
    queryset = BoardGameList.objects.all()
    template_name = "list/library.html"
    context_object_name = 'boardgamelists'


def update_library(request):
    print("this is the update_library")
    if request.method == 'POST':
        form = LibraryUpdateForm(request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.save()
            return redirect('update_library')
    else:
        form = LibraryUpdateForm()

    boardgamelists = BoardGameList.objects.all()
    context = {
        'boardgamelists': boardgamelists,
        'form': form,
    }
    print(context)
    return render(request, 'list/library.html', context)

