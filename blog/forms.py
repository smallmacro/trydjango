from django import forms

from .models import Article


class ArticleModelForm(forms.ModelForm):
    """docstring for ArticleModelForm"forms.ModelForm def __init__(self, arg):
        super(ArticleModelForm,forms.ModelForm.__init__()
        self.arg = arg
        """
    title = forms.CharField(widget=forms.TextInput(
                            attrs={
                                "placeholder":"Your title",
                                
                                }
                            )
                    )
    author = forms.CharField(widget=forms.TextInput(
                            attrs={
                                "placeholder":"Your name",
                                
                                }
                            )
                    )
    

    class Meta:
        model = Article
        fields = [
            'title',
            'author',
            'edit_time',
            'content',
            
        ]

    