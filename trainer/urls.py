from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_word_pair/', views.add_word_pair, name='add_word_pair'),
    path('word_pairs_list/', views.word_pairs_list, name='word_pairs_list'),
    path('practice/', views.practice, name='practice'),
    path('check_translation/<int:word_pair_id>/', views.check_translation, name='check_translation'),
]
