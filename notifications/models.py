from django.db import models
from django.contrib.auth import get_user_model

class Notification(models.Model):
    RECEPCIONISTAS = [
        ('amanda', 'Amanda González'),
        ('wanda', 'Wanda Pastor'),
    ]

    fecha_recepcion = models.DateField()
    hora_recepcion = models.TimeField()
    entidad_emisora = models.CharField(max_length=255)
    numero_expediente = models.CharField(max_length=100)
    dirigido_a = models.CharField(max_length=255)
    recepcionista = models.CharField(max_length=20, choices=RECEPCIONISTAS)
    entregado_a = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    fecha_entrega = models.DateField(null=True, blank=True)
    hora_entrega = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.numero_expediente} - {self.entidad_emisora}"
