from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cpf_cnpj = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name