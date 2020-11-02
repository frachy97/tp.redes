"""polygon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from apps.myApp.views import services, about_us, our_team, results, tsp, shortest_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', services, name="services"),
    path('about_us/', about_us, name='about_us'),
    path('our_team/', our_team, name='our_team'),
    path('results/', results, name='results'),
    path('tsp/', tsp, name='tsp'),
    path('shortest_path/', shortest_path, name='shortest_path'),
]
