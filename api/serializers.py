from .models import UserDetail

from rest_framework import serializers

from .models import *


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'


class UserShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserShare
        fields = "__all__"


class UserTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTransaction
        fields = "__all__"


class UserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWallet
        fields = "__all__"


class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userfollow
        fields = "__all__"


class UserContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContent
        fields = "__all__"
