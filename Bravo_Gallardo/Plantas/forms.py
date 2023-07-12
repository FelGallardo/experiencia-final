from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Productos


class RegistroUserForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput(attrs={
                                                                                        'placeholder':'Ingrese su nombre de usuario..',
                                                                                        'id':'username',
                                                                                        'class':'form-control',}), 
                                                                                        error_messages={})
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'Placeholder':'******************',
                                                                                      'id':'password1',
                                                                                      'class':'form-control',}), 
                                                                                      error_messages={})
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput(attrs={'Placeholder':'******************',
                                                                                                'id':'password2',
                                                                                                'class':'form-control',}), 
                                                                                                error_messages={})
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels ={
            'username':'Nombre de usuario',
            'password1':'Contraseña',
            'password2':'Repita la contraseña'
        }
        widgets={
            'username':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese su nombre de usuario..',
                    'id':'username',
                    'class':'form-control',
                }
            ),
            'password1':forms.PasswordInput(
                attrs={
                    'Placeholder':'Ingrese la contraseña',
                    'id':'password1',
                    'class':'form-control',
                }
            ),
            'password2':forms.PasswordInput(
                attrs={
                    'Placeholder':'Ingrese la contraseña',
                    'id':'password2',
                    'class':'form-control',
                }
            )
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['idprod','nombreproduc','descripcion','imagen','precio','stock']
        labels ={
            'idprod':'Id del Producto',
            'nombreproduc' : 'Nombre del Producto',
            'descripcion': 'Descipcion',
            'imagen':'Imagen',
            'precio':'Precio',
            'stock':'stock'
        }
        widgets={
            'idprod':forms.NumberInput(
                attrs={
                    'placeholder':'Ingrese el id del producto',
                    'id':'idprod',
                    'class':'form-control',
                    

                }
            ),
            'nombreproduc':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese el nombre del producto',
                    'id':'nombreproduc',
                    'class':'form-control',
                }
            ),
            'descripcion':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese una descripcion para el producto',
                    'id':'descripcion',
                    'class':'form-control',
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen',
                }
            ),
            'precio':forms.NumberInput(
                attrs={
                    'placeholder':'Ingrese un precio..',
                    'id':'precio',
                    'class':'form-control',
                }
            ),
            'stock':forms.NumberInput(
                attrs={
                    'placeholer':'Ingrese el stock',
                    'id':'stock',
                    'class':'form-control',
                }
            )
        }
