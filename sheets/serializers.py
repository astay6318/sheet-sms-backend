from rest_framework import serializers
from .models import Response
from .models import Form,Answer,Question

#to validate the request body

class Form_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class Question_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class Answer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class Response_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'