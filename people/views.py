from django.shortcuts import render
from .models import Person
from django.db import connection
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.urls import reverse

# Create your views here.
# def search_preparations(request):
# 	qs = Person.objects.all()

# 	if prep := request.GET.get('prep'):
# 		qs = qs.filter(prep__icontains=prep)
# 	if group := request.GET.get('group'):
# 		qs = qs.filter(group__icontains=group)
# 	if level := request.GET.get('level'):
# 		qs = qs.filter(level__iexact=level)
# 	if ptype := request.GET.get('type'):
# 		qs = qs.filter(type__iexact=ptype)

# 	return render(request, 'search.html', {'persons' : qs})

@login_required
def search_preparations(request):
    print("GET parameters:", request.GET)  # Debug output
    
    qs = Person.objects.all()
    
    # Debug: Print initial queryset count
    print("Initial queryset count:", qs.count())
    
    if prep := request.GET.get('prep'):
        qs = qs.filter(prep__icontains=prep)
        print("After prep filter:", qs.count())
        
    if group := request.GET.get('group'):
        qs = qs.filter(group__icontains=group)
        print("After group filter:", qs.count())
        
    if level := request.GET.get('level'):
        qs = qs.filter(level__iexact=level)
        print("After level filter:", qs.count())
        
    if ptype := request.GET.get('type'):
        qs = qs.filter(type__iexact=ptype)
        print("After type filter:", qs.count())
    
    return render(request, 'search.html', {'persons': qs})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('search_preparations')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form})

@ensure_csrf_cookie
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            host = request.get_host().split('.')[0]
            
            if host == 'start':
                return redirect(reverse('portal', urlconf='start.urls'))
            elif host == 'lists':
                # Use the correct URL name with namespace
                return redirect(reverse('search', urlconf='people.urls'))  # Changed from 'search_preparations'
                
        return render(request, 'login.html', {'form': form})
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    
   
