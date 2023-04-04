from django.forms import ModelForm
from cadastro.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['descricao','tipo','vencimento','valor','pago']        
      