from django.contrib import admin
from .models import*

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','descricao','tipo','vencimento','valor','pago')
    list_display_links = ('id','descricao')
    #list_filter = ('nome','sobrenome')
    list_per_page = 10
    search_fields = ('id','descricao')
    #list_editable = ('nome')

admin.site.register(Usuario,UsuarioAdmin)
