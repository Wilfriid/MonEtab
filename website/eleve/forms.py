from django import forms

class StudentForm(forms.Form):
    GENDER_CHOICES = [
        ('H', 'Homme'),
        ('F', 'Femme'),
    ]

    SCHOLARSHIP_CHOICES = [
        ('6eme', '6ème'),
        ('5eme', '5ème'),
        ('4eme', '4ème'),
        ('3eme', '3ème'),
        ('2nde', '2nde'),
        ('1ere', '1ère'),
        ('Tle', 'Terminale'),
    ]

    first_name = forms.CharField(label='Prénom', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Prénom'}))
    last_name = forms.CharField(label='Nom', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
    age = forms.IntegerField(label='Âge', widget=forms.NumberInput(attrs={'placeholder': 'Âge'}))
    country = forms.CharField(label='Ville', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Ville'}))
    phone = forms.CharField(label='Téléphone', max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Téléphone'}))
    gender = forms.ChoiceField(label='Genre', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    scholarship = forms.ChoiceField(label='Classe', choices=SCHOLARSHIP_CHOICES, widget=forms.Select)
    matricula = forms.CharField(label='Matricule', max_length=12, widget=forms.TextInput(attrs={'placeholder': 'Matricule'}))

   
from django import forms
from .models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'country', 'phone', 'gender', 'scholarship', 'matricula']
        labels = {
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'age': 'Âge',
            'country': 'Ville',
            'phone': 'Téléphone',
            'gender': 'Genre',
            'scholarship': 'Classe',
            'matricula': 'Matricule',
        }
        widgets = {
            'age': forms.NumberInput(attrs={'placeholder': 'Âge'}),
            'country': forms.TextInput(attrs={'placeholder': 'Ville'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Téléphone'}),
            'gender': forms.RadioSelect(choices=Student.GENDER_CHOICES),
            'scholarship': forms.Select(choices=Student.SCHOLARSHIP_CHOICES),
            'matricula': forms.TextInput(attrs={'placeholder': 'Matricule'}),
        }

