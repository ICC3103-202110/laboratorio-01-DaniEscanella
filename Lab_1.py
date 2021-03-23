def imprimir_mesa(largo,ancho):
    for i in range(largo+1):
        fila1="   "
        fila2=" "
        for k in range(ancho):
            fila1+=str(k)+" "
            if i!=0:
                fila2+="* "
        if i==0:
            print(fila1)
            
        elif i>0 and i<11:
            print(" "+str(i-1)+fila2)
        else:
            print(str(i-1)+fila2)



mazo=int(input("Inserte mazo:"))
cartas=mazo*2

imprimir_mesa(20,10)