from django.forms import ModelForm
from .models import Republica, Imagem

class RepublicaForms(ModelForm):
    class Meta:
        model = Republica
        fields = ['nome_republica','cidade','bairro','rua','numero_da_republica','valor','quantidade_de_quartos','quantidade_de_banheiros','quantidade_de_vagas_garagem','regras_da_republica','contato','nome_do_anunciante','descricao']
