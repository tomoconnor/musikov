from django.db import models

class MidiChain(models.Model):
	fileName = models.CharField(max_length=255)
	filePath = models.CharField(max_length=255)
	rank = models.IntegerField(default=100)
	transitionMatrix = models.TextField() #Pickle Target
	noteMapping = models.TextField()
	inverseNoteMapping = models.TextField()
	transitionFrequencies = models.TextField()
	transitionSum = models.FloatField()
	pngFile = models.CharField(max_length=255)
	svgFile = models.CharField(max_length=255)
	dotFile = models.CharField(max_length=255)


	def __str__(self):
			return self.fileName
	def get_rank(self):
			return (self.rank - 100)

class UploadedFile(models.Model):
	uploadfile = models.FileField(upload_to='uploads/%Y/%m/%d')
