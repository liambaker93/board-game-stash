from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import BoardGameList
from .forms import LibraryUpdateForm, LibraryEditForm
# Create your views here.


class HomePage(generic.TemplateView):
    template_name = "list/index.html"




def game_detail(request, slug):
    game = get_object_or_404(BoardGameList, slug=slug)
    return render(request, 'list/full_detail.html', {'game': game})


def update_library(request):

    if request.method == 'POST':
        form = LibraryUpdateForm(request.POST)
        if form.is_valid():
            messages.success(request, "Game successfully added to library!")
            new_game = form.save(commit=False)
            new_game.author = request.user
            new_game.save()
            return redirect('update_library')
        else:
            return redirect('update_library')
    else:
        form = LibraryUpdateForm()
        messages.error(request, "Error updating form, please try again.")

    boardgamelists = BoardGameList.objects.filter(author=request.user)
    context = {
        'boardgamelists': boardgamelists,
        'form': form,
    }
    return render(request, 'list/library.html', context)


def library_edit(request, game_id):
    """
    This provides a form for the user to edit a post of a game they've uploaded. 
    LibraryEditForm provides fewer options to edit than adding a new post, for example LibraryEdit won't allow the user to change the name of the game as that 
    would be handled by adding a new game to the library, however they can edit the number of players if they realise they inputted the wrong number.
    """
    game = get_object_or_404(BoardGameList, pk=game_id)

    if request.method == 'POST' and game.author == request.user:
        form = LibraryEditForm(request.POST, instance=game)
        if form.is_valid():
            messages.success(request, "Game editing...")
            form.save()
            messages.success(request, "Game updated!")
            return redirect('update_library')
    else:
        form = LibraryEditForm(instance=game)

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'list/edit_library.html', context)


def library_delete(request, game_id):

    game = get_object_or_404(BoardGameList, pk=game_id)

    if request.method == 'POST' and game.author == request.user:
        game.delete()
        messages.success(request, "Game deleted.")
        return redirect('update_library')
    
    context = {
        'game': game,
    }

    return render(request, 'list/delete_library.html', context)