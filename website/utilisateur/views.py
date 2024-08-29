from django.shortcuts import render , get_object_or_404,redirect
from .forms import UserForm , User
from django.contrib import messages

# Create your views here.
def utilisateur(request):
    users = User.objects.all()

    context = {'users': users}
    return render(request, "utilisateur.html", context)


def ajout_utilisateur(request):
    if request.method == 'POST':  
        form = UserForm(request.POST)
        if form.is_valid():  
            form.save()  
            return redirect('utilisateur:index')
            
    else:
        form = UserForm()  

    context = {'form': form}
    return render(request, "ajout_utilisateur.html", context)




def modi_utilisateur(request, id):
    user = get_object_or_404(User, id=id)  

    
    context = {
        "title": "Modifier utilisateur"
    }

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)  
        if form.is_valid():
            form.save()
            return redirect('utilisateur:index')  
    else:
        form = UserForm(instance=user) 
    
    
    context['form'] = form

    return render(request, "modi_utilisateur.html", context)


def suppr_utilisateur(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, "Utilisateur supprimé avec succès!")
    return redirect('utilisateur:index')