from django import forms

from .models import Category, Mushroom

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
    pass

class MushroomAEditForm(MushroomBaseForm):
    pass

class MushroomDeleteForm(MushroomBaseForm):
    pass