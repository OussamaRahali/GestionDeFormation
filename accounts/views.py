from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm,LoginForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Formateur, Formation, Etudiant, Registration,CustomUser
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.


def home(request):
    print('home view reached')
    return render(request, 'index.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def formateur_home(request):
    return render(request, 'formateur_home.html')

def etudiant_home(request):
    return render(request, 'etudiant_home.html')


def Signup(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.save()
            Etudiant.objects.create(user=user)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'An error occured during registration')
    else:
        form = CustomRegistrationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

    

""" def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'admin':
                    return redirect('admin_home')
                elif user.role == 'formateur':
                    return redirect('formateur_home')
                elif user.role == 'etudiant':
                    return redirect('etudiant_home')
            else:
                messages.error(request, 'Invalid credentials')
    return render(request, 'login.html', {'form': form})
 """
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('zab')
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user = authenticate(request, email=user_email, password=user_password)
        if user is not None:
            LoginPage(request, user)
            messages.success(request, f'Successfully logged in as {user.email}')
            if user.role == 'admin':
                return redirect('admin_home')
            elif user.role == 'formateur':
                return redirect('formateur_home')
            elif user.role == 'etudiant':
                return redirect('etudiant_home')
        else:
            messages.error(request, "Invalid credentials")
    else:
        if request.user.is_authenticated:
            messages.info(request, f"You are already logged in as {request.user.email}.")
            return redirect('zab')
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('home')  # or redirect to any other desired page

def zab(request):
    messages.info(request, f"You are already logged in as {request.user.email}.")
    return render(request, 'zab.html')