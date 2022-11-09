from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from django.utils import timezone

from category.models import Category
from user.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'title',
        )

    def create(self, validated_data):
        user = get_object_or_404(User, id=self.context['request'].user.id)

        return Category.objects.create(user=user, name=validated_data['title'])

    def update(self, instance, validated_data):
        instance.updated = timezone.now()

        if instance.custom:
            return super().update(instance, validated_data)