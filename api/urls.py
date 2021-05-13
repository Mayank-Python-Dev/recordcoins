from django.urls import path
from . import views

# Patterns
urlpatterns = [
    path('create-user/', views.CreateUserDetail, name='createuser'),
    path('update-user/<int:pk>/', views.UpdateUserDetail, name='updateuser'),
    path('delete-user/<int:pk>/', views.DeleteUserDetail, name='deleteuser'),

    path('user-details/', views.UserDetailList, name='userslist'),
    path('user-details/<int:pk>/',
         views.UserDetailListwithid, name='userslistwithid'),

    path('createshare/', views.CreateUserShare, name='createshare'),
    path('updateshare/<int:pk>/', views.UpdateUserShare, name='updateshare'),
    path('sharedetails', views.ShareDetails, name='sharedetails'),
    path('createtransaction/', views.CreateUserTransaction,
         name='createtransaction'),
    path('updatetransaction/<int:pk>/',
         views.UpdateUserTransaction, name='updatetransaction'),
    path('transactiondetails/', views.TransactionDetails,
         name='transactiondetails'),

    path('walletdetails/', views.WalletDetails, name='walletdetails'),
    # userfollow
    path('CreateUserfollow/', views.createuserfollow, name="createfollow"),
    path('DeleteUserfollow/<int:pk>/',
         views.deleteuserfollow, name="deletefollow"),
    path('DetailUserfollow/', views.detailuserfollow, name="detailfollow"),

    path('CreateUsercontent/', views.createusercontent, name="createcontent"),
    path('DetailUsercontent/', views.detailusercontent, name="detailcontent"),

]
