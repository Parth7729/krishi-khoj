from django.shortcuts import redirect, render, redirect
from .models import CustomUser, TractorDetails
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def register(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            user = CustomUser.objects.create_user(email=email, name=name, password=password)
            user.save()

            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
    except:
        pass

    return redirect('/')

def userlogin(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('email')
            password = request.POST.get('password')

            if CustomUser.objects.filter(email=username).exists():
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
    except:
        pass

    return redirect('index')

def signout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('index')

@login_required(login_url='index')
def addtractor(request):
    if request.method == 'POST':
        choices = request.POST.getlist('choices[]')
        color = request.POST.get('color')
        model = request.POST.get('model')
        if choices != []:
            TractorDetails.objects.create(user=request.user, implements=choices, color=color, model=model)
            return redirect('index')

    return render(request, 'main/add_tractor.html')

def alltractors(request):
    tractors = TractorDetails.objects.all().order_by('-id')
    context = {'tractors':tractors}

    return render(request, 'main/all_tractors.html', context)

def tractor_details(request, id=None):
    tractor = TractorDetails.objects.get(id=id)
    context = {'tractor':tractor}

    return render(request, 'main/tractor_details.html', context)