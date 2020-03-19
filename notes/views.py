from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, TemplateView, DetailView
from .models import Note
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import NoteForm
from django.urls import reverse_lazy


class NoteListView(LoginRequiredMixin, ListView):
	model = Note
	template_name = 'note.html'
	login_url = 'login'

class NoteCreateView(LoginRequiredMixin, CreateView):
	model = Note
	template_name = 'note_new.html'
	form_class = NoteForm
	success_url = reverse_lazy('note_list')
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class HomePageView(TemplateView):
	template_name = 'index.html'


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Note
	form_class = NoteForm
	template_name = 'note_edit.html'
	success_url = reverse_lazy('note_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Note
	template_name = 'note_delete.html'
	success_url = reverse_lazy('note_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user

class NoteDetailView(LoginRequiredMixin, DetailView):
	model = Note
	template_name = 'note_detail.html'
	login_url = 'login'



