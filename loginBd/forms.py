from django import forms
from . models import RegistrarUsuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = RegistrarUsuario
        fields = [
            'name',
            'lastname',
            'user',
            'email',
            'password',
            # 'repeatpassword',
            
        ]

