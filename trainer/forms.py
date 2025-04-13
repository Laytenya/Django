from django import forms
from .models import WordPair

class AddWordPairForm(forms.ModelForm):
    class Meta:
        model = WordPair
        fields = ['english_word', 'russian_word']

    def clean_english_word(self):
        english_word = self.cleaned_data.get('english_word')
        if not english_word or not english_word.isalpha():
            raise forms.ValidationError("English word must contain only letters and not be empty.")
        return english_word

    def clean_russian_word(self):
        russian_word = self.cleaned_data.get('russian_word')
        if not russian_word or not russian_word.isalpha():
            raise forms.ValidationError("Russian word must contain only letters and not be empty.")
        return russian_word

class TranslationForm(forms.Form):
    translation = forms.CharField(label="Your Translation", max_length=200)

    def clean_translation(self):
        translation = self.cleaned_data.get('translation')
        if not translation:
            raise forms.ValidationError("Translation cannot be empty.")
        return translation
