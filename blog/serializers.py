from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):

	image = serializers.ImageField(max_length=None, use_url=True)
	
	class Meta:
	    model = Blog
	    fields = ('id', 'title', 'image', 'description')
