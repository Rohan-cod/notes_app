from django.urls import path

from .views import NoteListView, MyNoteListView, NoteCreateView, HomePageView, NoteDeleteView, NoteUpdateView, NoteDetailView, search_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('mynotes/', MyNoteListView.as_view(), name='my_notes_list'),
    path('new/', NoteCreateView.as_view(), name='note_new'),
    path('<int:pk>/',
         NoteDetailView.as_view(), name='note_detail'),
    path('<int:pk>/delete/',
         NoteDeleteView.as_view(), name='note_delete'),
    path('<int:pk>/edit/',
         NoteUpdateView.as_view(), name='note_edit'),
    path('search/', search_view, name='search'),
]