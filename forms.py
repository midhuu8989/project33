#from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from .models import student
#from .models import User
#class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username","email","password1","password2")
#class studentform(UserCreationForm):
    #class Meta:
        #model=student
        #fields=("name","name","profile_pic")
