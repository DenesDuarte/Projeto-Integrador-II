from django import forms
from portal.models import Autor, Editora, Formato

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        exclude = ()

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})

        }

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        exclude = ()

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        
class FormatoForm(forms.ModelForm):
    class Meta:
        model = Formato
        exclude = ()

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}), 
        }