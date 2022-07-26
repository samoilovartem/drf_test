import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import FamousWomen

# class FamousWomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

"""Model based serializer (less code)"""


class FamousWomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = FamousWomen
        fields = '__all__'


"""Not a model based serializer (more code)"""


# class FamousWomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     created_on = serializers.DateTimeField(read_only=True)
#     updated_on = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     category_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return FamousWomen.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.updated_on = validated_data.get('updated_on', instance.updated_on)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.category_id = validated_data.get('category_id', instance.category_id)
#         instance.save()
#         return instance

# def encode():
#     model = FamousWomenModel('Angelina Jolie', 'Angelina Jolie')
#     model_sr = FamousWomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = FamousWomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
