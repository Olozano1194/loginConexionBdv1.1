from django.shortcuts import render, redirect, get_object_or_404
from . forms import UsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import RegistrarUsuario


import bcrypt  #esto nos sirve para encriptar la contraseña...ojo debemos instalarla pip install bcrypt 
# from django.http import HttpResponse

# Create your views here.

def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    else:
        user = authenticate(request, username=request.POST['user'], password=request.POST['password'])

        if user is None:
            return render(request, 'login.html', { 'error': 'Username or password in incorrect'})
        
        else:
            login(request, user)
            user_profile = RegistrarUsuario.objects.get(user=user)
            request.session['user_name'] = f'{user_profile.name} {user_profile.lastname}'

            return redirect('welcome')

def welcome(request):
    return render(request, 'welcome.html')

def registerBd(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password']
            hashed_password= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            usuario = form.save(commit=False)
            usuario.password= hashed_password
            usuario.save()
            # form.save()
    else:
        form = UsuarioForm()
    return render(request, 'checkIn.html')

def singoff(request):
    logout(request)
    return redirect('login')

def formcheckin(request):
    if request.method == 'GET':
        return render(request, 'checkIn.html')
    
    else:
        if request.POST['password'] == request.POST['repeatpassword']:
            try:
                user = User.objects.create_user(username=request.POST['user'], password=request.POST['password'])
                registerBd(request)
                user.save()
                login(request,user)
                return redirect('login')

            except IntegrityError:
                render(request, 'checkIn.html', { 'error': 'Usuario ya existe'}) 
        # return render(request, 'checkIn.html', { 'error': 'Error en el formulario'})
        
        return render(request, 'checkIn.html', { 'error': 'Password do not match'})    

def home(request):
    UserList = RegistrarUsuario.objects.all()

    return render(request, 'read.html', {'user': UserList})

def delete_user(request,id):
    usuario= RegistrarUsuario.objects.get(id=id)
    usuario.delete()

    return redirect('read')

def update_user(request, id):
    usuario= RegistrarUsuario.objects.get(id=id)

    return render(request,'update.html', {'user': usuario})

def actualizar(request, id):

    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        user = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpassword']

        usuario= RegistrarUsuario.objects.get(id=id)
        usuario.name = name
        usuario.lastname = lastname
        usuario.user = user
        usuario.email = email

        if not password:
            usuario.save()
            return redirect('read')

        # # Validación de contraseña
        # if password != repeatpassword:
        #     # Las contraseñas no coinciden, se muestra un mensaje de error
        #     errorMessage = 'Password do not match'

        if password == repeatpassword:
            
            hashed_password= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            usuario.password = hashed_password
            usuario.save()
            return redirect('read')
        
        else:
            errorMessage = 'Password do not match'
            return render(request, 'update.html', {'error': errorMessage, 'user': usuario})

            
        # usuario = RegistrarUsuario.objects.get(id=id)
        
    else:
        update_user(request, id)

