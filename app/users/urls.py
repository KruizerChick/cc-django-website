from django.urls import path, include
# from rest_framework import routers

from . import views


app_name = 'users'


urlpatterns = [
    path('~redirect/', view=views.user_redirect_view, name='redirect'),
    path('~update/', view=views.user_update_view, name='update'),
    path('<str:username>/', view=views.user_detail_view, name='detail'),

]
