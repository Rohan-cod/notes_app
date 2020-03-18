from django.views.generic import ListView, TemplateView
from .models import Note
from django.views.generic.edit import CreateView
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

