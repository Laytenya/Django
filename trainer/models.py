from django.db import models

class WordPair(models.Model):
    english_word = models.CharField(max_length=200)
    russian_word = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.english_word} - {self.russian_word}"
