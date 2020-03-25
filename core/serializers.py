from rest_framework import serializers
from .models import Category
from rest_framework_recursive.fields import RecursiveField
class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    class Meta:
        model = Category
        fields = "__all__"