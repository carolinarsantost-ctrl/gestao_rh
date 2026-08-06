from django.db import models

class Documento(models.Model):
    decricao = models.CharField(max_length=100)

    def __str__(self):
        return self.decricao
