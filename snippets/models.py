from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    slug = models.CharField(max_length=50, unique=True, verbose_name="slug")

    class Meta:
        verbose_name = "Lenguaje"
        verbose_name_plural = "Lenguajes"
    
    def __str__(self):
        return self.name

class Snippet(models.Model):
    user = models.ForeignKey(User, verbose_name="usuario", on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True, verbose_name="creado")
    updated = models.DateField(auto_now_add=True, verbose_name="editado")
    name = models.CharField(max_length=255, verbose_name="name")
    description = models.TextField(verbose_name="descripción")
    snippet = models.TextField(verbose_name="snnipet")
    languages = models.ForeignKey(Language, verbose_name="lenguaje", on_delete= models.CASCADE)
    public = models.BooleanField(default=False, verbose_name="¿Público?")

    class Meta:
        verbose_name = "Snippet"
        verbose_name_plural = "Snippets"