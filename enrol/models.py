from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Enrol(models.Model):

	name = models.CharField(max_length=15, verbose_name='Имя')
	surname = models.CharField(max_length=15, verbose_name='Фамилия')
	added = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='Телефон') 
	list_procedures = models.ManyToManyField('price.Price', verbose_name='Процедуры')
	wish_comment = models.TextField(max_length=10240, verbose_name='Комментарий')

	def get_procedures(self):
		return (['(' + p.title + ') ' for p in self.list_procedures.all()])
	get_procedures.short_description = 'Какие процедуры хотят сделать'	

	def get_full_name(self):
		return(self.name + ' ' + self.surname)
	get_full_name.short_description = 'Имя'

	class Meta:
		verbose_name = 'Запись'
		verbose_name_plural = 'Запись'