from django.db import models

class Usuario(models.Model):
    descricao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    vencimento = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=0)
    pago = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.descricao


