def sum():
    num=int(input("¿Cúantos valores se ingresarán?: "))
    lista=[]
    for x in range(0,num):
        n=int(input("-->"))
        lista.append(n)
    suma=0
    for x in lista:
        suma+=x
    print("La suma es ",suma,".")


def res():
    num=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    if num>num2:
        ras=num-num2
        print("La resta de ambos números es ",ras,".")
    else:
        if num2>num:
            ras=num2-num
            print("La resta de ambos números es ",ras,".")
        else:
            print("Ambos números son iguales por lo que la resta es 0")

def mul():
    num=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    if num==0 or num2==0:
        print("Uno de los números es 0 por lo que el producto de ambos es 0")
    else:
        print("El producto de la multiplicación de ",num," y ",num2," es ",num2*num,".")

def di():
    num=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    if num==0 or num2==0:
        print("No hay números divisibles entre 0")
    else:
        print("La división de ",num," entre ",num2," es ",num/num2,".")

def ab():
    num=float(input("Ingrese el primer valor: "))
    if num<0:
        num2=num*-1
        print("El valor absoluto de ",num," es ",num2,".")
    else:
        print("Es el mismo valor")

def may():
    num=int(input("¿Cúantos valores se ingresarán?: "))
    lista=[]
    for x in range(0,num):
        n=int(input("-->"))
        lista.append(n)
    print("El mayor valor es ",max(lista),".")

def men():
    num=int(input("¿Cúantos valores se ingresarán?: "))
    lista=[]
    for x in range(0,num):
        n=int(input("-->"))
        lista.append(n)
    print("El menor valor es ",min(lista),".")

def ig():
    num=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    if num==num2:
        print("Ambos números son iguales.")
    else:
        print("Los números no son iguales.")

def df():
    num=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    if num!=num2:
        print("Ambos números son diferentes.")
    else:
        print("Los números son iguales.")

def fi():
    num=int(input("¿Hastá que número?: "))
    n1,n2=0,1
    while n2<num:
        print(n2)
        n1,n2=n2,n1+n2

def fac():
    num=int(input("Ingrese el número: "))
    lista=[]
    for x in range (1,num+1):
        if num%x==0:
            lista.append(x)
    for x in lista:
        print(x)

def mcd():
    num=int(input("Ingrese el primer número: "))
    num2=int(input("Ingrese le segundo número: "))
    if num>num2:
        mayor=num
        menor=num2
    else:
        mayor=num2
        menor=num
    ct=1
    for x in range(2,menor+1):
        while num%x==0 and num2%x==0:
            ct*=x
            num/=x
            num2/=x
    print("El MCD de ambos números es ",ct,".")

def mcm():
    num=int(input("Ingrese el primer número: "))
    num2=int(input("Ingrese le segundo número: "))
    if num>num2:
        mayor=num
        menor=num2
    else:
        mayor=num2
        menor=num
    ct=1
    ctd=1
    for x in range(2,menor+1):
        while num%x==0 and num2%x==0:
            ct*=x
            num/=x
            num2/=x
    ctd=int((mayor*menor)/ct)
    print("El MCM de ambos números es: ",ctd,".")

def pro():
    num=int(input("¿Cúantos valores se ingresarán?: "))
    lista=[]
    for x in range(0,num):
        n=int(input("-->"))
        lista.append(n)
    suma=0
    for x in lista:
        suma+=x
    print("El promedio es ",suma/len(lista),".")