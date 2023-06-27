from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    """
    Форма создания блога
    """
    class Meta:
        model = Blog
        fields = ('title', 'body')
        widgets = {
            'body': forms.Textarea(attrs={'cols': 70, 'rows': 20}),
        }