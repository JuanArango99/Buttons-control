from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard_view(request):
    context={}
    return render(request,'app/dashboard.html', context)

@login_required
def user_view(request):
    context={}
    return render(request,'app/users.html', context)