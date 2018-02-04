from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import PlaceForm


# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def library(request):
    return render(request, 'library.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            Error = 'Something went wrong!'

    return render(request, 'login.html', {})


def create(request):
    if request.method == 'POST':
        place_form = PlaceForm(request.POST)
        if place_form.is_valid():
            place = place_form.save(commit=False)
            place.save()
            return redirect('/')
        else:
            error = 'Data is invalid!'

    place_form = PlaceForm()
    return render(request, 'create.html', {'place_form': place_form})
