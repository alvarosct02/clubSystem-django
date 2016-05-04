from django.db import models

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    ubicacion = models.CharField(max_length=200)

class TipoBungalow(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    precio = models.FloatField()
    aforo = models.IntegerField()

class TipoActividad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    precio = models.FloatField()

class TipoEvento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)

class TipoServicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)

class TipoDocumentoDePago(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)

class TipoMembresia(models.Model):
    nombre = models.CharField(max_length=100)
    numeroMaximoInitados = models.IntegerField()
    precio = models.FloatField()
    tipoCobro = models.CharField(max_length=100)

class TipoMulta(models.Model):
    nombre = models.CharField(max_length=100)
    razon = models.TextField(max_length=400)
    precio = models.FloatField()

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)





class Bungalow(models.Model):
    tipoBungalow = models.ForeignKey("TipoBungalow", on_delete=models.CASCADE)
    ambiente = models.ForeignKey("Ambiente", on_delete=models.CASCADE)

    estado = models.IntegerField()
    ubicacion = models.CharField(max_length=200)
    numero = models.IntegerField()

class Actividad(models.Model):
    tipoActividad = models.ForeignKey("TipoActividad", on_delete=models.CASCADE)
    ambiente = models.ForeignKey("Ambiente", on_delete=models.CASCADE)

    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    asistencia = models.IntegerField()
    precio = models.FloatField()

class Ambiente(models.Model):
    sede = models.ForeignKey("Sede", on_delete=models.CASCADE)
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    aforo = models.IntegerField()
    estado = models.IntegerField()

class Evento(models.Model):
    tipoEvento = models.ForeignKey("TipoEvento", on_delete=models.CASCADE)
    
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    asistencia = models.IntegerField()
    precio = models.FloatField()
    estado = models.IntegerField()