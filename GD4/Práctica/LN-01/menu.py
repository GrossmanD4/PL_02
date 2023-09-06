def suma(n1,n2):
    print("La suma es ",n1+n2,".")
def resta(n1,n2):
    if n1>n2:
        print("La resta es ",n1-n2,".")
    else:
        print("La resta es ",n2-n1,".")
def mult(n1,n2):
    print("El producto es ",n1*n2,".")
    
print("Menú interactivo: ")
print("Suma:1 ")
print("Resta:2 ")
print("Multiplicación:3 ")
print("División:Fuera de servicio")

def llamar(rpt=145):
    a=int(input("Ingrese el primer valor: "))
    b=int(input("Ingrese el segundo valor: "))
    while rpt>=4 or rpt<=0:
        rpt=int(input("Ingrese su elección: "))        
    if rpt==1:
        suma(a,b)
    elif rpt==2:
        resta(a,b)
    elif rpt==3:
        mult(a,b)
    else:
        print("Ingrese una elección válida")

llamar()
