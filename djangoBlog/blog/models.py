from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	#title field that's a characterfield(max_length=100)
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	#if user deletes account, it will delete all their posts with cascade
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


