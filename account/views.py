from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Account
from .serializers import AccountSerializer, AccountCreateSerializer


# Create your views here.


@api_view(['GET', 'POST'])
def list_accounts(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = AccountCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == "GET":
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = AccountCreateSerializer(account, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view()
def deposit(request):





# @api_view()
# def account_detail(request, pk):
#     try:
#         account = Account.objects.get(pk=pk)
#         serializer = AccountSerializer(account)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Account.DoesNotExist:
#         return Response({"message": "Account does not exist"},
#                         status=status.HTTP_404_NOT_FOUND)
