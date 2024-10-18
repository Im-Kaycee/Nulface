from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
def user_login(request):
    if request.method == "POST":
         username = request.POST["username"]
         password = request.POST["password"]
         user = authenticate(request, username=username, password=password)
         if user is not None:
          login(request, user)
          success_login = True
        # Redirect to a success page.
          messages.success(request, ('Login Successful'))
          return redirect('blog')
     
         else:
          messages.success(request, ("There was an error, Try again"))
          return redirect('user_login')
    
    else:
     return render(request, 'authenticate/login.html', {})
    
class user_register(generic.CreateView):
  form_class = UserCreationForm
  template_name = 'authenticate/register.html'
  success_url = reverse_lazy('login')

def logout_user(request):
  logout(request)
  messages.success(request, ('Logout Successful'))
  return redirect('index')