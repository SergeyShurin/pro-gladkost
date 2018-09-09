from django.db import models

# Create your models here.

class Price (models.Model):

	title = models.CharField(max_length=50, verbose_name='Название услуги')

	def __str__(self):
		return self.title

	price_man = models.IntegerField(blank=True, null=True, verbose_name='Цена для мужчин')
	price_woman = models.IntegerField(blank=True, null=True, verbose_name='Цена для женщин')
	time = models.IntegerField(blank=True, null=True, verbose_name='Время процедуры')

	class Meta:
		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуги'