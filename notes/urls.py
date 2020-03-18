from django.urls import path

from .views import NoteListView, NoteCreateView, HomePageView, NoteDeleteView, NoteUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('new/', NoteCreateView.as_view(), name='note_new'),
    path('<int:pk>/delete/',
         NoteDeleteView.as_view(), name='note_delete'),
    path('<int:pk>/edit/',
         NoteUpdateView.as_view(), name='note_edit'),
]