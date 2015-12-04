# coding: utf-8

from django.db import models
from django.contrib.auth.models import User


class Rol(models.Model):
	rol = models.CharField(max_length=20, unique=True)
	descripcion = models.TextField()
	def __unicode__(self):
		return self.rol

class Perfiles(models.Model):
	SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
	usuario = models.OneToOneField(User)
	telefono = models.IntegerField()
	dni = models.CharField(max_length=8)
	rol = models.ForeignKey(Rol)
	sexo = models.CharField(choices=SEX, max_length=255,blank=True, verbose_name='Género')
	direccion = models.CharField(max_length=150)
	telefono = models.CharField(max_length=13)
	estado = models.BooleanField(default=True)
	imagen = models.ImageField(upload_to='perfiles')
	def __unicode__(self):
		return self.usuario.username
		#return ‘%s %s’ % (self.usuario.username, self.usuario.first_name)
