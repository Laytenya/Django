from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddWordPairForm, TranslationForm
from .models import WordPair
import random
from django.utils.translation import gettext as _

def home(request):
    return render(request, 'trainer/home.html')

def add_word_pair(request):
    if request.method == 'POST':
        form = AddWordPairForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('word_pairs_list')
    else:
        form = AddWordPairForm()
    return render(request, 'trainer/add_word_pair.html', {'form': form})

def word_pairs_list(request):
    word_pairs = WordPair.objects.all()
    return render(request, 'trainer/word_pairs_list.html', {'word_pairs': word_pairs})

def practice(request):
    word_pairs = list(WordPair.objects.all())
    if not word_pairs:
        return render(request, 'trainer/practice.html', {'message': _("No words added yet. Add some words first!")})

    word_pair = random.choice(word_pairs)
    return render(request, 'trainer/practice.html', {'word_pair': word_pair})

def check_translation(request, word_pair_id):
    word_pair = get_object_or_404(WordPair, pk=word_pair_id)
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            translation = form.cleaned_data['translation']
            if translation.lower() == word_pair.russian_word.lower():
                message = _("Correct!")
            else:
                message = _("Incorrect. Correct translation: ") + word_pair.russian_word
            return render(request, 'trainer/result.html', {'message': message, 'word_pair': word_pair})
    else:
        form = TranslationForm()
    return render(request, 'trainer/translation_form.html', {'form': form, 'word_pair': word_pair})
