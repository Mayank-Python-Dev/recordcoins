from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('dashboardMainPage/', views.dashboardMainPage, name='dashboardMainPage'),
    path('InvestmentPage/', views.InvestmentPage, name='InvestmentPage'),
    path('ScrenerPage/', views.ScrenerPage, name='ScrenerPage'),
    path('SavedContent/', views.SavedContent, name='SavedContent'),
    path('StatisticsPage/', views.StatisticsPage, name='StatisticsPage'),
    path('ExplorerPage/', views.ExplorerPage, name='ExplorerPage'),
    path('StatesPage/', views.StatesPage, name='StatesPage'),
    # path('logout/', views.logout, name='logout'),

]
