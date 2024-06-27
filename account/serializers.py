from rest_framework import serializers
from .models import Account, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'transaction_type', 'transaction_status', 'description', 'amount']


class AccountSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)

    class Meta:
        model = Account
        fields = ['account_number', 'first_name', 'last_name', 'account_balance', 'account_type', 'transactions']


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'pin', 'account_type']
# account_number = serializers.CharField(max_length=10)
# first_name = serializers.CharField(max_length=255)
# last_name = serializers.CharField(max_length=255)
# account_balance = serializers.DecimalField(max_digits=6, decimal_places=2)
# account_type = serializers.CharField(max_length=10)
