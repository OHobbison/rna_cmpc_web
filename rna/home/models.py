from django.db import models

# Create your models here.

#Modelo de teste para aprender / excluir depois
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    ip_address = models.GenericIPAddressField(null=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    


class Id_hub(models.Model):
    CD_PROC_IMPORTA_HUB=models.CharField(max_length=50)
    CD_IMPORTACAO_HUB=models.CharField(max_length=50)
    CD_NIVEL=models.CharField(max_length=50)
    CD_MEDICAO=models.CharField(max_length=50)
    CD_MEDICAO_PLANTIO=models.CharField(max_length=50)
    CD_MEDICAO_PARCELA=models.CharField(max_length=50)
    ID_REGIAO=models.CharField(max_length=50)
    ID_PROJETO=models.CharField(max_length=50)
    CD_TALHAO=models.CharField(max_length=50)
    NRO_PARCELA=models.CharField(max_length=50)
    NUM_FILA=models.CharField(max_length=50)
    NUM_ARVORE=models.CharField(max_length=50)
    NUM_FUSTE=models.CharField(max_length=50)
    TIP_ARV=models.CharField(max_length=50)
    CAP=models.CharField(max_length=50)
    HT= models.CharField(max_length=50)

    def __str__(self):
        return f'{self.CD_IMPORTACAO_HUB}'
    
