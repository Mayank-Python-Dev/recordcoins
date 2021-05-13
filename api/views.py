from django.shortcuts import render

from django.http import JsonResponse

from rest_framework.decorators import api_view

from rest_framework.response import Response

from .serializers import UserDetailSerializer

from .models import *

from .serializers import *
# views


@api_view(['POST'])
def CreateUserDetail(request):
    serializer = UserDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def UpdateUserDetail(request, pk):
    Detail = UserDetail.objects.get(id=pk)
    serializer = UserDetailSerializer(instance=Detail, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def UserDetailListwithid(request, pk):
    Detail = UserDetail.objects.get(id=pk)
    serializer = UserDetailSerializer(Detail)

    return Response(serializer.data)


@api_view(['GET'])
def UserDetailList(request):
    Detail = UserDetail.objects.all()
    serializer = UserDetailSerializer(Detail, many=True)

    return Response(serializer.data)


@api_view(['DELETE'])
def DeleteUserDetail(request, pk):
    Detail = UserDetail.objects.get(id=pk)
    Detail.delete()

    return Response({'Deleted Successfully'})


@api_view(['POST'])
def CreateUserShare(request):
    serializer = UserShareSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def UpdateUserShare(request, pk):
    Share = UserShare.objects.get(id=pk)
    serializer = UserShareSerializer(instance=Share, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def ShareDetails(request):
    Share = UserShare.objects.all()
    serializer = UserShareSerializer(Share, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def CreateUserTransaction(request):
    serializer = UserTransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def UpdateUserTransaction(request, pk):
    transaction = UserTransaction.objects.get(id=pk)
    serializer = UserTransactionSerializer(
        instance=transaction, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def TransactionDetails(request):
    transaction = UserTransaction.objects.all()
    serializer = UserTransactionSerializer(transaction, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def WalletDetails(request):
    Wallet = UserWallet.objects.all()
    serializer = UserWalletSerializer(Wallet, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def createuserfollow(request):
    serializer = UserFollowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteuserfollow(request, pk):
    Detail = Userfollow.objects.get(id=pk)
    Detail.delete()

    return Response({'Deleted Successfully'})


@api_view(['GET'])
def detailuserfollow(request):
    Detail = Userfollow.objects.all()
    serializer = UserFollowSerializer(Detail, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def createusercontent(request):
    serializer = UserContentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def detailusercontent(request):
    Detail = UserContent.objects.all()
    serializer = UserContentSerializer(Detail, many=True)

    return Response(serializer.data)
