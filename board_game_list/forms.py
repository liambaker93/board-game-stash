from .models import BoardGameList
from django import forms 


class LibraryUpdateForm(forms.ModelForm):
    class Meta:
        model = BoardGameList
        fields = ('title', 'category', 'description', 'rating', 'image', 'minplayers', 'maxplayers')


class LibraryEditForm(forms.ModelForm):
    class Meta:
        model = BoardGameList
        fields = ('category', 'description', 'rating', 'minplayers', 'maxplayers')