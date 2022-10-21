from contextlib import nullcontext
from operator import length_hint
from random import choices
from django.db import models

product_status = [
    (1, 'Si'),
    (2, 'No')
]

# Create your models here.
class Tarea(models.Model):
    tarea = models.CharField(max_length = 100)
    status = models.IntegerField(
        null=False,blank=False,
        choices=product_status,
        default=2,
    )

    def __str__(self):
        return self.tarea

