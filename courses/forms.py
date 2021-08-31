from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
                            attrs={
                                "placeholder":"Your course title",
                                
                                }
                            )
                    )
    class Meta:
        model = Course
        fields = [
        'title',
        'publisher',
        'release_date'
        ]