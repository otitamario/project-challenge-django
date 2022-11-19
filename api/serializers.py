from rest_framework import serializers
from accounts.models import Project
from django.contrib.auth import get_user_model


class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    #fields = '__all__'
    fields =["title","zip_code","cost","deadline"]

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = '__all__'
