from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import BoardGameList
from .forms import LibraryUpdateForm, LibraryEditForm
# Create your views here.

class HomePage(generic.TemplateView):
    template_name = "list/index.html"



def view_library(request):
    user_library_games = request.user.library_games.all()
    context = {
        'user_library_games': user_library_games
    }
    return render(request, 'list/library.html', context)


def game_detail(request, slug):
    game = get_object_or_404(BoardGameList, slug=slug)
    return render(request, 'list/full_detail.html', {'game': game})


def add_game_to_global_library(request, game_id):
    game = get_object_or_404(BoardGameList, game_id)
    if request.method == 'POST':
        game.added_by.add(request.user)
        return redirect('list')
    
    return redirect('list')


def update_library(request):

    game_id_exists = request.GET.get('prepopulate_game')

    if game_id_exists:
        try:
            game_prepopulate = BoardGameList.objects.get(pk=game_id_exists)
            form = LibraryUpdateForm(instance=game_prepopulate)
        except BoardGameList.DoesNotExist:
            pass

    if request.method == 'POST':
        form = LibraryUpdateForm(request.POST)
        if form.is_valid():
            messages.success(request, "Game successfully added to library!")
            new_game = form.save(commit=False)
            new_game.author = request.user
            new_game.save()
            print("Adding game to library...")
            return redirect('update_library')
        else:
            print("Form is NOT valid. Errors:")
            print(form.errors)
            print("Form error validation not complete")
    else:
        form = LibraryUpdateForm()
        messages.error(request, "Error updating form, please try again.")


    boardgamelists = BoardGameList.objects.filter(author=request.user)
    context = {
        'boardgamelists': boardgamelists,
        'form': form,
    }
    print(context)
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
            print("Form is valid, attempting to save...")
            form.save()
            print("Database update successful!")
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
        return redirect('update_library')

    return render(request, 'list/delete_library.html', {'game': game})