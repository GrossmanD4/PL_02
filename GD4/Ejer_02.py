from paquete.funciones import *
rpta="1"
lista=["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
while rpta!="2":
    print("¿Qué función desea usar?:")
    print("1=Sumar")
    print("2=Restar")
    print("3=Multiplicar")
    print("4=Dividir")
    print("5=Módulo")
    print("6=Mayor")
    print("7=Menor")
    print("8=Igualdad")
    print("9=Desigualdad")
    print("10=Fibonacci")
    print("11=Factorial")
    print("12=Máximo Común Divisor")
    print("13=Mínimo Común Múltiplo")
    print("14=Promedio")
    ele=str(input("---> "))
    while ele not in lista:
        ele=str(input("---> "))
    if ele=="1":
        sum()
    elif ele=="2":
        res()
    elif ele=="3":
        mul()
    elif ele=="4":
        di()
    elif ele=="5":
        ab()
    elif ele=="6":
        may()
    elif ele=="7":
        men()
    elif ele=="8":
        ig()
    elif ele=="9":
        df()
    elif ele=="10":
        fi()
    elif ele=="11":
        fac()
    elif ele=="12":
        mcd()
    elif ele=="13":
        mcm()
    elif ele=="14":
        pro()
    print("1:Continuar")
    print("2:Finalizar el programa")
    rpta=str(input("-->"))
    while rpta!="1" and rpta!="2":
        rpta=str(input("--->"))