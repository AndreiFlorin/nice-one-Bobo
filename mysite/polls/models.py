from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
	text=models.CharField(max_length=200)
	date=models.DateTimeField('Buna buna apasa apasa')



	def __repr__(self):
		return '<{} - {} >'.format(self.id,self.text)

	def __str__(self):
		return self.text

	def was_published_recently(self):
		return self.date >= timezone.now() - datetime.timedelta(days=1)

		was_published_recently.admin_order_field='date'
		was_published_recently.boolean= True
		was_published_recently='Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.choice_text