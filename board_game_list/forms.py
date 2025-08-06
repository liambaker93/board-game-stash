from .models import BoardGameList
from django import forms 

class LibraryUpdateForm(forms.ModelForm):
    class Meta:
        model = BoardGameList
        fields = ('title', 'category', 'description', 'rating', 'image')