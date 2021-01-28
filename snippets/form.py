from django import forms
from .models import Snippet, Language


#choices = [('Python', 'Python'), ('JavaScript', 'JavaScript'), ('C++', 'C++')]
choices = Language.objects.all().values_list('name','name')



class FormSnippet(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['user','name','description','languages','public', 'snippet']

        widgets = {
            'languages': forms.Select(choices=choices, attrs={'class':'form-control'})
        }
