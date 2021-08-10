from django.contrib import admin

from .models import Usuario


@admin.register(Usuario)
class usuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'cpf', 'situacao')
    search_fields = ('cpf',)

