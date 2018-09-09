from django.db import models

from django.core.validators import RegexValidator

# Create your models here.

class Good(models.Model):
	name = models.CharField(max_length=50, verbose_name='Название')

	def __str__(self):
		return self.name

	price = models.IntegerField(default=0, verbose_name='Цена')
	image = models.ImageField(upload_to="image/", verbose_name='Изображение')
	description = models.TextField(max_length=10240, verbose_name='Описание')

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

class OrderItem(models.Model):
	name = models.ForeignKey(Good, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)

class Order(models.Model):
	customer_name = models.CharField(max_length=15, verbose_name='Имя')
	customer_surname = models.CharField(max_length=15, verbose_name='Фамилия')
	paid = models.BooleanField(default=False, verbose_name='Оплачено')
	added = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')
	order_item = models.ManyToManyField(OrderItem, verbose_name='Заказ')
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='Телефон') 

	def get_products(self):
		return (['(' + p.name.name + ' x'  + str(p.quantity) + ')' for p in self.order_item.all()])
	get_products.short_description = 'Название товара и его количество в заказе'	

	def get_full_name(self):
		return(self.customer_name + ' ' + self.customer_surname)
	get_full_name.short_description = 'Имя'

	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'