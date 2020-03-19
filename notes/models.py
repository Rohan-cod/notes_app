from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

class Note(models.Model):
	text = models.CharField(max_length=120)
	created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
		)

	def __str__(self):
		return self.text


	def get_absolute_url(self):
		return reverse('note_detail', args=[str(self.id)])
