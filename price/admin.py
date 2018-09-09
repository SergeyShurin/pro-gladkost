from django.contrib import admin

# Register your models here.

from .models import Price

class PriceAdmin(admin.ModelAdmin):
	list_display = ('title', 'time', 'price_man', 'price_woman')
	fields = ('title', 'time', 'price_man', 'price_woman')

admin.site.register(Price, PriceAdmin)