from django.db import models
from apps.inventario.models import *
from django.conf import settings
from django.core.validators import RegexValidator
# Create your models here.

#class tipoPago(models.Model):

class Metas(models.Model):
	monto_asignado = models.DecimalField(max_digits=6, decimal_places=2)
	descripcion = models.CharField(max_length=50)

	def __str__(self):
		return '%s'%(self.monto_asignado)

class Empleado(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
	meta_asignadafk = models.ForeignKey(Metas, on_delete=models.CASCADE,null=True)
	nombres = models.CharField(max_length=40,null=False)
	apellidos = models.CharField(max_length=40,null=False)
	telefono= models.CharField(max_length=8,null=False,unique=True,validators=[
		RegexValidator(regex='^.{8}$', 
		message='Ha introducido un numero incorrecto', 
		code='nomatch'
	)])
	dui = models.CharField(max_length=9,null=False,unique=True)
	nit = models.CharField(max_length=14,null=False,unique=True)
	def __str__(self):
		return '%s'%(self.nombres)

class Asignacion(models.Model):
	meta_asignadafk = models.ForeignKey(Metas, on_delete=models.CASCADE,null=False)	
	empleadofk = models.ForeignKey(Empleado, on_delete=models.CASCADE,null=False)
	fecha_asignacion = models.DateField(auto_now=True)
	monto_logrado = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)


class pedido(models.Model):
	finalizada =models.BooleanField(default=False)
	fechaCreada =models.DateField(auto_now=True)
	vendedor = models.ForeignKey(Empleado, on_delete=models.CASCADE,null=True)
	cliente = models.CharField(max_length=50,null=True)
	total = models.DecimalField(max_digits=6,decimal_places=2,null=True)
	#tipoPago = models.foreignKey(tipoPago, on_delete=models.CASCADE)
	def setVendedor(self, valor):
		self.vendedor=valor
	def setCliente(self, valor):
		self.cliente=valor
	def setTotal(self, valor):
		self.total=self.total+valor
	def setFinal(self):
		self.finalizada=True

class lineaDeVenta(models.Model):
	articulofk = models.ForeignKey(Producto, on_delete=models.CASCADE)
	pedidofk = models.ForeignKey(pedido, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=1)
	subtotal = models.DecimalField(max_digits=6,decimal_places=2,default=0)
	def setArticulo(self, valor):
		self.articulofk=valor
	def setPedido(self, valor):
		self.pedidofk=valor
	def setCantidad(self, valor):
		self.cantidad=valor
	def sub(self):
		self.subtotal=self.cantidad * self.articulofk.precioventa
	def getSubtotal(self):
		return self.subtotal

