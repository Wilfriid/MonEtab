from django import forms
from .models import Teacher

class TeacherForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
    prenom = forms.CharField(label='Prénom', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Prénom'}))
    
    MATIERE_CHOICES = [
        ('Maths', 'Maths'),
        ('Physique', 'Physique'),
        ('EPS', 'EPS'),
        ('Anglais', 'Anglais'),
        ('SVT', 'SVT'),
        ('français', 'Français'),
        ('philosophie', 'Philosophie'),
    ]
    matiere = forms.ChoiceField(label='Sélectionner une matière', choices=MATIERE_CHOICES)
    
    age = forms.IntegerField(label='Âge')
    telephone = forms.CharField(label='Téléphone', max_length=15)
    ville = forms.CharField(label='Ville', max_length=100)
    
    
class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'last_name', 'age', 'courses', 'number', 'ville']  
        labels = {
            'name': 'Nom',
            'last_name': 'Prénom',
             'age': 'Âge',
            'courses': 'Matière',
            'number': 'Téléphone',
            'ville': 'Ville',
        }
        widgets = {
            
            'courses': forms.Select(choices=[
                ('Maths', 'Maths'),
                ('Physique', 'Physique'),
                ('EPS', 'EPS'),
                ('Anglais', 'Anglais'),
                ('SVT', 'SVT'),
                ('français', 'Français'),
                ('philosophie', 'Philosophie'),
            ]),
        }
