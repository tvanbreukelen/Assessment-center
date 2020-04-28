from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def indexView(request):
    return render(request, 'examen/index.html')

def dashboardView(request):
    return render(request, 'examen/dashboard.html')

def registerView(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('examen-home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registration/register.html', {'form': form })
