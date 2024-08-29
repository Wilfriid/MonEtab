from django.urls import path
from .views import professeur,ajoutprofesseur ,modifierProf ,supp_prof


app_name='professeur'
urlpatterns = [
    path('', professeur, name='index'),
    path('ajoutprofesseur/', ajoutprofesseur, name='add'),
    path('modifierProf/<int:id>/', modifierProf, name='edit'),
    path('supp_prof/<int:id>/', supp_prof, name='delete'),
    


]