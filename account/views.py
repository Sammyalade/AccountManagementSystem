from datetime import datetime
from decimal import Decimal

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Account, Transaction
from .serializers import AccountSerializer, AccountCreateSerializer


# Create your views here.

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer




# class ListAccount(ListCreateAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountCreateSerializer
#
#
# class AccountDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountCreateSerializer


@api_view(["POST"])
def deposit(request):
    account_number = request.data['account_number']
    amount = Decimal(request.data['amount'])
    account = get_object_or_404(Account, pk=account_number)
    account.account_balance += amount
    account.save()
    Transaction.objects.create(
        account=account,
        amount=amount,
    )
    return Response(data={"message": "Transaction Successful"}, status=status.HTTP_200_OK)


@api_view(["PATCH"])
def withdraw(request):
    account_number = request.data['account_number']
    amount = request.data['amount']
    pin = request.data['pin']
    transaction_type = request.data['transaction_type']
    account = get_object_or_404(Account, pk=account_number)
    if account.pin == pin:
        if account.account_balance >= Decimal(amount):
            account.account_balance -= Decimal(amount)
            account.save()
            Transaction.objects.create(
                account=account,
                amount=amount,
                transaction_type=transaction_type
            )
            return Response(data={"message": "Withdrawal Successful"}, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Insufficient Balance"},
                            status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data={"message": "Incorrect pin"}, status=status.HTTP_400_BAD_REQUEST)

# @api_view()
# def account_detail(request, pk):
#     try:
#         account = Account.objects.get(pk=pk)
#         serializer = AccountSerializer(account)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Account.DoesNotExist:
#         return Response({"message": "Account does not exist"},
#                         status=status.HTTP_404_NOT_FOUND)


# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def account_detail(request, pk):
#     account = get_object_or_404(Account, pk=pk)
#     if request.method == "GET":
#         serializer = AccountSerializer(account)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "PUT":
#         serializer = AccountCreateSerializer(account, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     elif request.method == "DELETE":
#         account.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def list_accounts(request):
#     if request.method == 'GET':
#         accounts = Account.objects.all()
#         serializer = AccountSerializer(accounts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = AccountCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
