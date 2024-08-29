from django.urls import path
from .views import dashbord, connexion 

app_name='dashbord'
urlpatterns = [
    path('', dashbord, name='index'),  
    path('connexion/', connexion, name='connexion'),
  


]
