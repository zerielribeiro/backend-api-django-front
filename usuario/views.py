from django import forms
from django.shortcuts import render
from django.db.models import fields
from usuario.form import UsuarioForm
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Usuario

def UsuarioList(request):
    usuarios = Usuario.objects.all()
    return render (request, 'list-usuario.html' , {'usuarios': usuarios})



class UsuarioCreate(CreateView):
   model= Usuario
   fields= ['email', 'cpf']
   template_name= 'form.html'
   success_url = '/'

   def get_context_data(self, * args, **kwargs):
      context = super().get_context_data(*args, **kwargs)

      context['titulo'] = 'Cadastro de Usuarios'
      context['botao'] = 'Cadastrar'

      return context

class Usuarioupdate(UpdateView):
   model= Usuario
   fields= ['email', 'cpf', 'situacao']
   template_name= 'form.html'
   success_url = '/'

   def get_context_data(self, * args, **kwargs):
      context = super().get_context_data(*args, **kwargs)

      context['titulo'] = 'Atualização de Usuario'
      context['botao'] = 'Salvar'

      return context

class UsuarioDelete(DeleteView):
    model= Usuario
    template_name= 'form-exluir.html'
    success_url= '/'
