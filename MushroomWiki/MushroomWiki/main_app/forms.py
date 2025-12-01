from django import forms

from .models import Category, Mushroom
from django.forms.widgets import ClearableFileInput

class CustomClearableFileInput(ClearableFileInput):
    template_name = 'widgets/custom_clearable_file_input.html'


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryForm(CategoryBaseForm):
    pass

class MushroomBaseForm(forms.ModelForm):
    class Meta:
        model = Mushroom
        fields = '__all__'



class MushroomAddForm(MushroomBaseForm):
    class Meta(MushroomBaseForm.Meta):
        widgets = {
            'image': CustomClearableFileInput(attrs={
                'class': 'mushroom-image-input',
                'id': 'mushroom-image-upload',
                "image": forms.ClearableFileInput(attrs={"label": ""}),  # hides label

            }),
        }
class MushroomAEditForm(MushroomBaseForm):
    class Meta(MushroomBaseForm.Meta):
        widgets = {
            'image': CustomClearableFileInput(attrs={
                'class': 'mushroom-image-input',
                'id': 'mushroom-image-upload',
                "image": forms.ClearableFileInput(attrs={"label": ""}),  # hides label

            }),
        }


class MushroomDeleteForm(MushroomBaseForm):
    class Meta(MushroomBaseForm.Meta):
        model = Mushroom
        # explicitly list fields to show, excluding 'image'
        fields = ['name', 'category', 'description']
