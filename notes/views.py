from django.views.generic import ListView, TemplateView
from .models import Note
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import NoteForm
from django.urls import reverse_lazy


class NoteListView(ListView):
	model = Note
	template_name = 'note.html'

class NoteCreateView(CreateView):
	model = Note
	template_name = 'note_new.html'
	form_class = NoteForm
	success_url = reverse_lazy('note_list')

class HomePageView(TemplateView):
	template_name = 'index.html'


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_edit.html'
    success_url = reverse_lazy('note_list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_delete.html'
    success_url = reverse_lazy('note_list')



