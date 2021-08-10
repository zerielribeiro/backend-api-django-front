from django.db.models import fields
from rest_framework import serializers
from usuario import models


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Usuario
        fields= ('email','cpf','situacao')
