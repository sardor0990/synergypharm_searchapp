from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from people import views as people_views


app_name = 'start'

urlpatterns = [
		path('', views.portal, name='portal'),
		path('login/', people_views.custom_login, name='login'),
]
