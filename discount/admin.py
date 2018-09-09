from django.contrib import admin

# Register your models here.

from .models import Discount

class DiscountAdmin(admin.ModelAdmin):
	list_display = ('title',)
	fields = ('title', 'description', 'image')

admin.site.register(Discount, DiscountAdmin)