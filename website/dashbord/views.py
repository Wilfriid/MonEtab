from django.shortcuts import render

def dashbord(request):
    return render(request, "dashbord.html")


def connexion(request):
    return render(request, "connexion.html")



def deconnexion(request):
    return render(request, "deconnexion.html")