import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.urls import reverse
from app.models import Registro
from django.contrib.auth.views import LoginView
from datetime import datetime
from json import dumps
from datetime import timedelta
import pandas as pd
from django.contrib.auth.models import User



class MyLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        now=datetime.now()
        date_time_str = now.strftime("%d-%m-%Y %H:%M:%S")
        request.session['date'] =date_time_str 
        

        return super().dispatch(request, *args, **kwargs)

@login_required
def home_view(request):
    objs = []
    objs = Registro.objects.all()
    df = pd.DataFrame(list(objs.values('user','boton1','boton2')))
    df['user'] = df['user'].apply(lambda x: User.objects.get(pk=x).username )
    # print(df.head())
    #Botones
    sumabotones = []
    sumab1=sumab2=0
    for element in objs:
        sumab1 = element.boton1+sumab1
        sumab2 = element.boton2+sumab2
    sumabotones =[sumab1,sumab2]
    #Cantidad de logins
    usersLogins = df.pivot_table(columns=['user'], aggfunc='size')
    print(usersLogins)


    context={
        'objs':objs,
        'sumabotones':sumabotones,
        'usersLogins':usersLogins,
        
    }

    return render(request,'home.html',context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def create_register(request):
    if request.method =='GET':
        counter1=request.GET.get('counter1')
        counter2=request.GET.get('counter2')
        date=request.session['date'] 
        inicio = datetime.strptime(date,"%d-%m-%Y %H:%M:%S")
        now=datetime.now()
        tiempo = (now-inicio).total_seconds()
        tiempo = timedelta(seconds=tiempo)
        
        tiempo=str(tiempo).split(".")[0]
        registro = Registro(boton1=counter1,
                            boton2=counter2,
                            tiempo=tiempo,
                            inicio=inicio,
                            user=request.user)
        registro.save()
    return HttpResponse("correct")





