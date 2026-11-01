from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm


# login view
def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.success(request, ("There was an error logging in, Try again!!!"))
            return redirect('login_user') 
    
    return render(request, 'members/login.html', {})

# logout view
def logout_user(request):
    logout(request)
    return redirect('login_user')

# register user view
def register_user(request):
    form = UserCreationForm() 
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ("Registration is Successful"))
            return redirect('login_user')
        else:
            pass
    return render(request, 'members/register_user.html',{'form': form})
