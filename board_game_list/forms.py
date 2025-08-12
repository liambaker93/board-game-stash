from .models import BoardGameList
from django import forms 


class LibraryUpdateForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    
    class Meta:
        model = BoardGameList
        fields = ('title', 'category', 'description', 'rating', 'image', 'minplayers', 'maxplayers')


class LibraryEditForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    
    class Meta:
        model = BoardGameList
        fields = ('category', 'description', 'rating', 'image', 'minplayers', 'maxplayers')


class LibraryUpdateFormTest(forms.ModelForm):

    class Meta:
        model = BoardGameList
        fields = ('title', 'description', 'rating', 'minplayers', 'maxplayers')


class LibraryEditFormTest(forms.ModelForm):

    class Meta:
        model = BoardGameList
        fields = ('description', 'rating', 'minplayers', 'maxplayers')