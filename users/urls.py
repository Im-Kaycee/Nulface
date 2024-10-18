from django.urls import path
from . import views
from .views import user_register
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('login/', views.user_login, name='user_login'),
   path('register/', user_register.as_view(), name='register'),
   path('logout/', views.logout_user, name='logout'),

]
