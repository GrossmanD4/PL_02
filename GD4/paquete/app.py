
#DETECCIÓN TARJETA
def tarjeta():
    print("A continuación digite su número de tarjeta en la consola")
    tar=str(input("--->"))
    while len(tar)!=16:
        tar=str(input("Digite una número de tarjeta válida--->"))
    cl=str(input("Clave--->"))
    while len(cl)!=6:
        cl=str(input("Clave incorrecta--->"))
#IDENTIFICACIÓN
def ide():
    nume=["1","2","3","4","5","6","7","8","9","0"]

    nom=str(input("Ingrese su nombre: "))
    cont=0
    for x in nom:
        for y in nume:
            if x==y:
                cont+=1
    while cont!=0:
        nom=str(input("Ingrese un nombre válido: "))
        cont=0
        for x in nom:
            for y in nume:
                if x==y:
                    cont+=1

    ap=str(input("Ingrese su apellido: "))
    cont2=0
    for x in ap:
        for y in nume:
            if x==y:
                cont2+=1
    while cont2!=0:
        ap=str(input("Ingrese un apellido válido: "))
        cont2=0
        for x in ap:
            for y in nume:
                if x==y:
                    cont2+=1

    dni=str(input("Ingrese su DNI: "))
    cont3=0
    for x in dni:
        for y in nume:
            if x==y:
                cont3+=1
    while cont3!=8:
        dni=str(input("Ingrese un DNI correcto: "))
        cont3=0
        for x in dni:
            for y in nume:
                if x==y:
                    cont3+=1 
#MOSTRAR ARTICULOS Y RECOLECTAR EL PRECIO DE LO QUE SE VA COMPRAR
def men():
    frutas={"Melon":2,"Pera":4,"Manzana":5,"Sandía":2.5,"Ninguna":0}
    verduras={"Lechuga":3,"Espinaca":4,"Nabo":3.5,"Limon":20,"Ninguna":0}
    pres=0
    rpt="1"
    while rpt!="2":
        print("¿A qué sección le gustaria dirigirse?:")
        print("Frutas:1")
        print("Verduras:2")
        rt=round(float(input("-->")))
        while rt>=3 or rt<=0:
            rt=round(float(input("Ingrese una sección válida-->")))
        if rt==1:
            print("Frutas:")
            for x,y in frutas.items():
                print ("",x,":",y,"")
            el=str(input("Cuál desea comprar: "))
            while el not in frutas.keys():
                el=str(input("Ingrese un objeto válido: "))
            pres=pres+frutas[el]
        if rt==2:
            print("Verduras:")
            for x,y in verduras.items():
                print ("",x,":",y,"")
            eso=str(input("Cuál desea comprar: "))
            while eso not in verduras.keys():
                eso=str(input("Ingrese un objeto válido: "))
            pres=pres+verduras[eso]
        print("Contenido del carrito: ",pres,"")
        print("¿Le gustaría continuar con el programa de compra?: ")
        print("1: Continuar comprando")
        print("2: Finalizar compra")
        print("3: En el caso de querer rehacer la compra presione el botón")
        rpt=str(input("-->"))
        while rpt!="1" and rpt!="2" and rpt!="3":
            rpt=str(input("Ingrese una opción válida: "))
        if rpt=="3":
            pres=0
        if rpt=="2":
            presI=pres*0.17
            presT=pres+presI
            print("El precio total de los productos con el IGV inclupido sería de ",pres+presI,".")
    


    