from django.shortcuts import render ,redirect ,get_object_or_404
from .forms import StudentForm , StudentModelForm , Student
from django.contrib import messages

# Create your views here.

def ajout_eleve(request):
    
    eleves = Student.objects.all()  
    context = {'eleves': eleves}  
    return render(request, "ajout_eleve.html", context)

def form_ajouEleve(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eleve:index')
            
    else:
        form = StudentModelForm()  

    return render(request, 'form_ajouEleve.html', {'form': form})

def modifie_eleve(request, id):
    user = get_object_or_404(Student, id=id)  

    
    context = {
        "title": "Modifier eleve"
    }

    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=user)  
        if form.is_valid():
            form.save()
            return redirect('eleve:index')  
    else:
        form = StudentModelForm(instance=user) 
    
    
    context['form'] = form

    return render(request, "modifie_eleve.html", context)

def supprimer_eleve(request, id):
    user = get_object_or_404(Student, id=id)
    user.delete()
    messages.success(request, "eleve supprimé avec succès!")
    return redirect('eleve:index')

