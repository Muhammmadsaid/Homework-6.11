# Create your views here.
from django.shortcuts import render, redirect
from .models import Theme
from .forms import ThemeForm


def theme_list(request):
    themes = Theme.objects.all()
    return render(request, 'themes/theme_list.html', {'themes': themes})


def add_theme(request):
    if request.method == 'POST':
        form = ThemeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('theme_list')
    else:
        form = ThemeForm()
    return render(request, 'themes/add_theme.html', {'form': form})


def edit_theme(request, pk):
    theme = Theme.objects.get(pk=pk)
    if request.method == 'POST':
        form = ThemeForm(request.POST, instance=theme)
        if form.is_valid():
            form.save()
            return redirect('theme_list')
    else:
        form = ThemeForm(instance=theme)
    return render(request, 'themes/edit_theme.html', {'form': form})


def delete_theme(request, pk):
    theme = Theme.objects.get(pk=pk)
    if request.method == 'POST':
        theme.delete()
        return redirect('theme_list')
    return render(request, 'themes/delete_theme.html', {'theme': theme})
