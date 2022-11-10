from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from django.utils import timezone
from django.db.models import F

from transaction.models import Transaction
from category.models import Category
from user.models import User


class TransactionSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(write_only=True)

    class Meta:
        model = Transaction
        fields = (
            'trans_amount',
            'description',
            'organization',
            'category',
            'category_title',
        )
        read_only_fields = ('category',)


    def create(self, validated_data):
        user = get_object_or_404(User, id=self.context['request'].user.id)

        category = get_object_or_404(
            Category,
            user_id=user.id,
            title=validated_data['category_title'],
        )

        transaction = Transaction.objects.create(
            category=category,
            trans_amount=validated_data['trans_amount'],
            description=validated_data['description'],
            organization=validated_data['organization'],
        )

        category.amount = F('amount') + validated_data['trans_amount']
        category.save()

        if validated_data['category_title'] == 'Зарплата':
            user.user_balance = F('user_balance') + validated_data['amount']
        else:
            user.user_balance = F('user_balance') + validated_data['amount']

        user.save()

        return transaction

    def update(self, instance, validated_data):
        instance.updated = timezone.now()

        return super().update(instance, validated_data)