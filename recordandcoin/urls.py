from django.contrib import admin
from django.urls import path, include
from login.views import ListUsers, CustomAuthToken
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('recordandcoin/', include('mainproject.urls')),
    path('', include('login.urls')),
    path('api/users/', ListUsers.as_view()),
    path('api-token/', CustomAuthToken.as_view()),

]
