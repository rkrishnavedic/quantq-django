from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save();
            # log the user in
            
    form = UserCreationForm();
    return render(request, 'accounts/signup.html', {'form':form});

def login_view(request, slug):
    return render(request, 'accounts/login.html');