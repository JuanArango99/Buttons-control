"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view,create_register,MyLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('app/', include('app.urls', namespace='app')),
    path('login/', MyLoginView.as_view(template_name='auth/login.html' ), name='login'),
    # path('login/', user_login, name='login'),
    path('create-register/', create_register, name='create_register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)