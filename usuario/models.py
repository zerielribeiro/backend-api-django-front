from django.db import models


class Usuario(models.Model):

    STATUS_CHOICES =(
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo')
    )

    email = models.EmailField(max_length= 100, blank= False, null= False, unique= True)
    cpf = models.CharField(max_length=11, blank=False, null= False, unique= True)
    situacao = models.CharField(max_length= 7, choices=STATUS_CHOICES, default= 'ativo')

    def __str__(self):
        return self.email

