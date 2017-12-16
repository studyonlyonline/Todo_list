from django.db import models

# Create your models here.

class Task(models.Model):
	task_name = models.CharField(max_length=200)
	task_desc = models.TextField()
	due_date = models.DateTimeField()
	label = models.ForeignKey(
			'Label',
			on_delete= models.SET_NULL,
			null=True
		)

class Label(models.Model):
	LABEL_NAME = (
			('P','Personal'),
			('W','Work'),
			('S','Shopping'),
			('F','FInance'),
			('O','Others')
		)
	labelled = models.CharField(max_length=1, choices=LABEL_NAME, default='O')

class Status(models.Model):
	STATUS_VALUES = (
			('N','New'),
			('P', 'Progress'),
			('C', 'Completed')
		)
	status_set = models.CharField(max_length=1, choices=STATUS_VALUES,default='N')
	
