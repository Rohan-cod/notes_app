from django.urls import path

from .views import NoteListView, NoteCreateView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('new/', NoteCreateView.as_view(), name='note_new'),
]