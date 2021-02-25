from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#from.forms import UserForm,studentform

def home(request):
    return render(request,'home.html')
@login_required
def dashboard(request):
    return render(request,'dasboard.html')
def register(request):
    if request.method=="POST":
        form=UserCreationForm()
        if form.is_valid:
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

#def studentregister(request):
    #if request.method=="POST":
    #    form=UserCreationForm()
    #    if form.is_valid:
    #        form.save()
    #        return redirect('studentlogin')
    #else:
    #    form=UserCreationForm()
    #return render(request,'registration/register.html',{'form':form})
