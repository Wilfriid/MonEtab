from django.contrib import admin
from django.urls import path, include 
from dashbord import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eleve/', include("eleve.urls")),
    path('dashbord/', include('dashbord.urls')),  
    path('professeur/', include('professeur.urls')),
    path('rapport/', include('rapport.urls')),
    path('utilisateur/', include('utilisateur.urls')),
   
    path('deconnexion/', views.deconnexion, name='deconnexion'),
]
