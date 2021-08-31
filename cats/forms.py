from django import forms

from .models import Cat

class CatForm(forms.ModelForm):
    name       =    forms.CharField(widget=forms.TextInput(
                            attrs={
                                "placeholder":"Your cat's name",
                                "class" : "input-text",
                                "id" : "input-name",
                            }
                            )
                    )
    age        =    forms.DecimalField(initial=1)
    color      =    forms.ChoiceField(choices=Cat.CATS_COLOR)

    #customize form validation
    def clean_name(self, *arg, **kwargs):
        name = self.cleaned_data.get("name")
        if name.startswith("K"):
            raise forms.ValidationError("This is not a valid name") 

    #inherent from forms,ModelForm must have the class Meta
    class Meta:
        model = Cat
        fields = [
            'name',
            'age',
            'color',
            'description',
            'location',
            'owner'
        ]

# raw form
class RawCatForm(forms.Form):
    name       =    forms.CharField(widget=forms.TextInput(
                            attrs={
                                "placeholder":"Your cat's name",
                                "class" : "input-text",
                                "id" : "input-name",
                            }
                            )
                    )
    age        =    forms.DecimalField(initial=1)
    color      =    forms.ChoiceField(choices=Cat.CATS_COLOR)