from rest_framework import serializers

from .models import Users, Account, Transfers, Store


class UsersSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    surname = serializers.CharField(max_length=25)
    name = serializers.CharField(max_length=25)
    patronymic = serializers.CharField(allow_null=True, max_length=25)
    login = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    account_id = serializers.IntegerField()

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.name = validated_data.get('name', instance.name)
        instance.patronymic = validated_data.get('patronymic', instance.patronymic)
        instance.login = validated_data.get('login', instance.login)
        instance.password = validated_data.get('password', instance.password)
        instance.account_id = validated_data.get('account_id', instance.account_id)
        instance.save()
        return instance


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    card_number = serializers.IntegerField()
    csv = serializers.IntegerField()
    balance = serializers.FloatField()

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.card_number = validated_data.get('card_number', instance.card_number)
        instance.csv = validated_data.get('csv', instance.csv)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance

class TransferSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    sender_id = serializers.IntegerField()
    recipient_id = serializers.IntegerField()
    sum = serializers.FloatField()
    transfer_time = serializers.DateTimeField()

    def create(self, validated_data):
        return Transfers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.sender_id = validated_data.get('sender_id', instance.sender_id)
        instance.recipient_id = validated_data.get('recipient_id', instance.recipient_id)
        instance.sum = validated_data.get('sum', instance.sum)
        instance.transfer_time = validated_data.get('transfer_time', instance.transfer_time)
        instance.save()
        return instance

class StoreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    ingridient_id = serializers.IntegerField()
    price = serializers.FloatField()

    def create(self, validated_data):
        return Store.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.ingridient_id = validated_data.get('ingridient_id', instance.ingridient_id)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
