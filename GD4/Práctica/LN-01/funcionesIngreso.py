def detect(pal):
    num=["1","2","3","4","5","6","7","8","9","0"]
    cont=0
    for x in num:
        if x in pal:
            cont+=1
    if cont>0:
        print("Es número")
    else:
        print("No es número")

