from utilidades import impuestos
from utilidades import calculos
monto = int(input("Introduzca un monto entero: "))

print ("El impuesto IVA de 12%:", impuestos.impuesto_iva12(monto))
suma = int(input("Introduzca un monto entero a sumar: "))

print ("La suma total es:", calculos.suma_total(suma))
