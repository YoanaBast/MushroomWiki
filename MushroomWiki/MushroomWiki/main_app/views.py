from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models  import Category, Mushroom
from .forms import CategoryForm, MushroomAddForm, MushroomAEditForm, MushroomDeleteForm
# Create your views here.


def index_view(request):
    return render(request, 'common/index.html')


def create_category_view(request):
    if request.method == 'GET':
        form = CategoryForm()
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'categories/create-category.html', context)


def dashboard_view(request):
    mushrooms = Mushroom.objects.all()
    context = {'mushrooms': mushrooms}
    return render(request, 'common/dashboard.html', context)


def create_mushroom_view(request):
    if request.method == 'GET':
        form = MushroomAddForm()
    elif request.method == 'POST':
        form = MushroomAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'mushrooms/create-mushroom.html', context)


def delete_mushroom_view(request, pk):
    mushroom = Mushroom.objects.get(id=pk)
    if request.method == 'GET':
        form = MushroomDeleteForm(instance=mushroom)
    else:
        form = MushroomDeleteForm(request.POST, instance=mushroom)
        if form.is_valid():
            mushroom.delete()
            return redirect('dashboard')

    context = {'form': form, 'mushroom': mushroom}
    return render(request, 'mushrooms/delete-mushroom.html', context)


def details_mushroom_view(request, pk):
    mushroom = Mushroom.objects.get(id=pk)
    context = {'mushroom': mushroom}
    return render(request, 'mushrooms/details-mushroom.html', context)


def edit_mushroom_view(request, pk):
    mushroom = Mushroom.objects.get(id=pk)
    if request.method == 'GET':
        form = MushroomAEditForm(instance=mushroom)
    elif request.method == 'POST':
        form = MushroomAEditForm(request.POST, instance=mushroom)
        if form.is_valid():
            mushroom.save()
            return redirect('dashboard')
    context = {'form': form, 'mushroom': mushroom}
    return render(request, 'mushrooms/edit-mushroom.html', context)