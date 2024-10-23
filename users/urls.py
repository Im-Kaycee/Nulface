from django.urls import path
from . import views
from .views import user_register
from .views import user_edit
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView
urlpatterns = [
   path('login/', views.user_login, name='user_login'),
   path('register/', user_register.as_view(), name='register'),
   path('logout/', views.logout_user, name='logout'),
   path('edit_profile/', user_edit.as_view(), name='user_edit'),
   #path('password/', auth_views.PasswordChangeView.as_view(template_name = 'authenticate/change-password.html')),
   path('password/', PasswordsChangeView.as_view(template_name = 'authenticate/change-password.html')),
 
]
