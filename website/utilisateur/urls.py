from django.urls import path

from .views import  utilisateur ,ajout_utilisateur ,modi_utilisateur ,suppr_utilisateur

app_name='utilisateur'
urlpatterns = [
       path('', utilisateur, name='index'),
       path('ajout_utilisateur/', ajout_utilisateur, name='add'),
       path('modi_utilisateur/<int:id>/', modi_utilisateur, name='edit'),
       path('supprimer_utilisateur/<int:id>/', suppr_utilisateur, name='delete'),

]