from django.shortcuts import render, redirect

# Create your views here.

from django.http import JsonResponse

from rest_framework.decorators import api_view

from rest_framework.response import Response

from django.contrib.auth.models import User, auth


from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from users.models import CustomUser

from api.models import *

from .serializers import *

from login.decorators import *

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def index(request):
    return render(request, 'mainproject/index.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def dashboardMainPage(request):
    return render(request, 'mainproject/dashboardMainPage.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def InvestmentPage(request):
	shareuser = UserShare.objects.filter(Share_Owner = request.user)
	context = {'shareuser':shareuser}
	return render(request,'mainproject/dashboardInvestmentPage.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def ScrenerPage(request):
    return render(request, 'mainproject/dashboardScrenerPage.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def SavedContent(request):
    return render(request, 'mainproject/dashboardSavedContent.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def StatisticsPage(request):
    return render(request, 'mainproject/dashboardStatisticsPage.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def ExplorerPage(request):
    return render(request, 'mainproject/dashboardExplorerPage.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def StatesPage(request):
    return render(request, 'mainproject/dashboardStatesPage.html')

