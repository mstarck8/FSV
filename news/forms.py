from django import forms
from .models import NewsPost


class PostForm(forms.ModelForm):

    class Meta:
        model = NewsPost
        fields = ['header', 'created_at', 'content']
        labels = {
            'header': 'Überschrift',
            'created_at': 'Datum als JJJJ-MM-TT',
            'content': 'Inhalt',
        }
        widgets = {

        }
