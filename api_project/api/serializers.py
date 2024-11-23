from rest_framework import serializers
from api.models import Book
# Serializers definition
class BookSeliazer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'