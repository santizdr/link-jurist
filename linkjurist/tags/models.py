from django.db import models

# Create your models here.

class Tag(models.Model):
    SPECIALITIES = (
        ("PENAL", "Derecho penal"), ("CIVIL", "Derecho civil"), ("LABORAL", "Derecho laboral"),
        ("MERCANTIL", "Derecho mercantil"), ("ADMINISTRATIVO", "Derecho administrativo"), ("INTERNACIONAL", "Derecho internacional"),
    )

    tag = models.CharField(choices=SPECIALITIES)

    def __str__(self):
        return self.tag