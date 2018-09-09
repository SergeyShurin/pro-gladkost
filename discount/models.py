from django.db import models

# Create your models here.

class Discount (models.Model):
	title = models.CharField(max_length=50, verbose_name='Заголовок')

	def __str__(self):
		return self.title

	image = models.ImageField(upload_to="image/", verbose_name='Изображение')
	description = models.TextField(max_length=10240, verbose_name='Описание')

	class Meta:
		verbose_name = 'Акции'
		verbose_name_plural = 'Акции'