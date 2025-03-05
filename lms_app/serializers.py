from rest_framework import serializers
from .models import Member, Category, Book, Author


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # def create(self, validated_data):
    #     Book.objects.create(**validated_data)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 26b10013c2dc8ed0cb923d862cbc87a630d9a559
=======
>>>>>>> 6cfda09 (updated admin,models,serializers,urls)
