from django.urls import path
from .views import ajout_eleve, form_ajouEleve ,modifie_eleve ,supprimer_eleve 


app_name='eleve'
urlpatterns = [
    # definir ttes les routes qui sont specifique a l'app
    
    path('', ajout_eleve, name='index'),
    path('form_ajouEleve/', form_ajouEleve, name='add'),
    path('modifie_eleve/<int:id>/', modifie_eleve, name='edit'),
    path('supprimer_eleve/<int:id>/', supprimer_eleve, name='delete'),
    


]