from django.urls import path
from apps.myApp.views import services, about_us, our_team, results, tsp, shortest_path

urlpatterns = [
    path('', services, name='services'),
    path('about_us/', about_us, name='about_us'),
    path('our_team/', our_team, name='our_team'),
    path('results/', results, name='results'),
    path('tsp/', tsp, name='tsp'),
    path('shortest_path/', shortest_path, name='shortest_path'),
 
]
