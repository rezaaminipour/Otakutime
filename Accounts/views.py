from django.shortcuts import redirect,render
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from . import models
from .forms import CustomUserCreationForm,CustomUserChangeForm

from django.contrib.auth import get_user_model
User=get_user_model()

from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views import generic
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')

    else:
        form = CustomUserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()

            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))

            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        
        return redirect('home')

    return render(request,'../templates/Home.html')

@login_required(login_url="/accounts/login")
def edit_profile(request):
    
    if request.method == 'POST':
        form = CustomUserChangeForm(data=request.POST,instance=request.user ,files=request.FILES)
        if form.is_valid():
            
            form.save()
            return redirect('home')

    elif request.method == 'GET':
        print(request.user)
        form = CustomUserChangeForm(instance=request.user)

    context={'form':form}
    return render(request,'accounts/editprofile.html',context)


class ProfilePageView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'accounts/profile.html'

    def get_context_data(self,*args, **kwargs):
        
        context = super(ProfilePageView,self).get_context_data(*args, **kwargs)

        page_user =get_object_or_404(User,id=self.kwargs['pk'])

        
        context["page_user"] = page_user
        return context