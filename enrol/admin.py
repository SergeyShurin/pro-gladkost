from django.contrib import admin

# Register your models here.

from .models import Enrol

class EnrolAdmin(admin.ModelAdmin):
	readonly_fields = ('id', 'name', 'surname', 'list_procedures', 'phone', 'added', 'wish_comment')
	list_display = ('id', 'get_full_name', 'get_procedures', 'phone', 'added', 'wish_comment')

admin.site.register(Enrol, EnrolAdmin)