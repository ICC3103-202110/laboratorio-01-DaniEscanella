from numpy import random 
def generar_matrices(cartas,mazo):
    if cartas>10: 
        columns=10
        cant_lines=cartas//10
        if (cartas%10)!=0:
            cant_lines+=1
    else:
        columns=cartas
        cant_lines=2
    mazo_final=[]
    for j in range(cant_lines):
        one=[]
        for i in range(columns):
            if len(mazo)!=0:
                len_=len(mazo)
                random_=random.randint(len_)
                one.append(mazo[random_])
                mazo.pop(random_)
            else:
                one.append(" ")
        mazo_final.append(one)
    return mazo_final


        



def imprimir_mesa(mazo,mazo_falso,theone):
    contador=len(mazo)
    cont=0
    while contador!=0:
        coordenadas="  "
        fila=" "
        for k in range(theone):
            coordenadas+=str(k)+" "
            if contador==len(mazo):
                fila+=str(mazo_falso[cont][k])+" "
            
        if cont==0:
            print(coordenadas)
        elif cont>0 and cont<11:
            print(" "+str(cont-1)+fila)
        else:
            print(str(cont-1)+fila)



cartas=int(input("Inserte mazo:"))
if cartas>10:
    theone=10
else:
    theone=cartas
mazo=[]
mazo_falso=[]
for a in range(cartas):
    mazo.append(a+1)
    mazo.append(a+1)
    mazo_falso.append("*")
    mazo_falso.append("*")

print(mazo)
mazo=generar_matrices(cartas,mazo)
print(mazo)