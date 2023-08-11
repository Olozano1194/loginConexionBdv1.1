from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class RegistrarUsuario(models.Model):

    name = models.CharField(max_length=100)

    lastname = models.CharField(max_length=100)
    
    user = models.CharField(max_length=30, unique=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=300)


    def __str__(self):
        return self.name
    

# class UsuarioRegistrado(models.Model):

#     # user = models.OneToOneField(RegistrarUsuario, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     password = models.CharField(max_length=20)

# #función nos sirve para que en el django-admin nos aparezca el nombre del usuario o nombre que querramos en ves del .object
#     def __str__(self):
#         return self.user


