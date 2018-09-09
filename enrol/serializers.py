from rest_framework import serializers

from .models import Enrol

class EnrolSerializer(serializers.ModelSerializer):

	class Meta:
	    model = Enrol
	    fields = ('name', 'surname', 'list_procedures', 'added', 'phone', 'wish_comment')
