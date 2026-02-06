from django.db import models

class Togri(models.Model):
    soz = models.CharField(max_length=100, verbose_name="so'z")

    def __str__(self):
        return self.soz

    class Meta:
        verbose_name_plural = "Tog'ri so'zlar"
        verbose_name = "Tog'ri so'z"


class Notogri(models.Model):
    soz = models.CharField(max_length=100, verbose_name="so'z")
    togri = models.ForeignKey(Togri, on_delete=models.CASCADE)

    def __str__(self):
        return self.soz

    class Meta:
        verbose_name_plural = "Notog'ri so'zlar"
        verbose_name = "Notog'ri so'z"
