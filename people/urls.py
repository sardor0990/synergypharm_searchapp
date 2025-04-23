from django.urls import path
from .views import search_preparations, custom_login
from . import views
from django.contrib.auth import views as auth_views

app_name = 'people'

urlpatterns = [
		path('', search_preparations, name='search'),
		path('login/', views.custom_login, name='login'),
		path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
