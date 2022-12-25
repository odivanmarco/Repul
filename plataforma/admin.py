from django.contrib import admin
from .models import Republica, Imagem
# Register your models here.
@admin.register(Republica)
class republicaAdmin(admin.ModelAdmin):
    list_display = ('bairro', 'rua', 'cidade', 'valor', 'contato',)
    list_editable = ('valor', 'contato')
    list_filter = ('bairro', 'valor')


admin.site.register(Imagem)
