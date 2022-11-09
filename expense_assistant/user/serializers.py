from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import User
from category.models import Category


class UserSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'firstname',
            'lastname',
            'email',
            'password',
            'confirm_password',
        )

    auth_categories = (
        'Забота о себе',
        'Зарплата',
        'Здоровье и фитнес',
        'Кафе и рестораны',
        'Машина',
        'Образование',
        'Отдых и развлечения',
        'Платежи, комиссии',
        'Покупки: одежда, техника',
        'Продукты',
        'Проезд',
    )

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            user_email=validated_data['user_email'],

        )

        user.set_password(validated_data['password'])

        for category in self.auth_categories:
            Category.objects.create(user=user, name=category)

        user.save()

        return user

    def validate(self, params):
        if params['password'] != params['confirm_password']:
            raise serializers.ValidationError({'detail': 'Incorrect password input. Passwords do not match'})

        return params


class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )
        extra_kwargs = {'password': {'write_only': True}}

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'firstname',
            'lastname',
            'balance',
            'email',
        )