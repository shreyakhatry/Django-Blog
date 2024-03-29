from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterform
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
          form = UserRegisterform(request.POST)
          if form.is_valid():
               form.save()
               username=form.cleaned_data.get('username')
               messages.success(request,f'Your account has been created as {username}!')
               return redirect('login')
          
    else:
        form = UserRegisterform()

    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
     return render(request,'users/profile.html')
