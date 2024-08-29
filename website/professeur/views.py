from django.shortcuts import render ,get_object_or_404 ,redirect 
from .forms import TeacherForm , Teacher,TeacherModelForm
from django.contrib import messages

# Create your views here.

def professeur(request):
    professeurs = Teacher.objects.all()  # Utilisez le modèle Teacher pour récupérer tous les enseignants
    context = {'professeurs': professeurs}  
    return render(request, "professeur.html", context)


def ajoutprofesseur(request):
    if request.method == 'POST':
        form = TeacherModelForm(request.POST)
        if form.is_valid():
           
            form.save()
            
            
    else:
        form = TeacherModelForm()

    return render(request, 'ajoutprofesseur.html', {'form': form})



def modifierProf(request, id):
    user = get_object_or_404(Teacher, id=id)  

    
    context = {
        "title": "Modifier professeur"
    }

    if request.method == "POST":
        form = TeacherModelForm(request.POST, instance=user)  
        if form.is_valid():
            form.save()
            return redirect('professeur:index')  
    else:
        form = TeacherModelForm(instance=user) 
    
    
    context['form'] = form

    return render(request, "modifierProf.html", context)




def supp_prof(request, id):
    user = get_object_or_404(Teacher, id=id)
    user.delete()
    messages.success(request, "Professeur supprimé avec succès!")
    return redirect('professeur:index')

