from django.db import models


# Create your models here.
class Pays(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Sexe(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    sexe = models.ForeignKey(Sexe, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return self.surname


class Colis(models.Model):
    poids = models.DecimalField(verbose_name=None, max_digits=5, decimal_places=2)
    description = models.TextField()
    commande = models.ForeignKey('Commande', on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Commande(models.Model):
    reference = models.IntegerField(null=False)
    created_at = models.DateField(auto_now_add=True)
    terminated = models.BooleanField(default=False)
    price = models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.name