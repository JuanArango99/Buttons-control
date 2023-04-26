from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registro(models.Model):
    boton1 = models.IntegerField(default=0)
    boton2 = models.IntegerField(default=0)
    tiempo = models.TimeField(default=0)
    inicio = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return(str(self.user))
        
