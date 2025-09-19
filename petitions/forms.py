from django import forms
from .models import Petition


class PetitionForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Movie title you want added"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Why should we add this movie? (optional)"}),
        }
