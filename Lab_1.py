import random 
def generar_matrices(cartas,mazo):
    if (cartas)>10: 
        columns=10
        cant_lines=cartas//10
        if (cartas%10)!=0:
            cant_lines+=1
    else:
        columns=cartas//2
        cant_lines=2
    mazo_final=[]
    for j in range(cant_lines):
        one=[]
        for i in range(columns):
            if len(mazo)!=0:
                one.append(mazo[0])
                mazo.pop(0)
            else:
                one.append(" ")
        mazo_final.append(one)
    return mazo_final

def print_mesa(mazo):
    for k in range(len(mazo)):
        coordenadas="   "
        fila=" "
        for j in range(len(mazo[0])):
            coordenadas+=str(j)+"  "
            fila+=str(mazo[k][j])+"  "
        if k==0:
            print(coordenadas)
            print(" "+str(k)+fila)
            
        elif k>0 and k<11:
            print(" "+str(k)+fila)
        else:
            print(str(k)+fila)


def playing(mazo,mazo_falso,puntos):
    play_1=str(input("Elija su primera coordenada: ej: 1,0 "))
    play_1=play_1.split(",")
    aa=mazo_falso[int(play_1[1])][int(play_1[0])]
    mazo_falso[int(play_1[1])][int(play_1[0])]=mazo[int(play_1[1])][int(play_1[0])]
    print_mesa(mazo_falso)
    play_2=str(input("Elija su segunda coordenada: "))
    play_2=play_2.split(",")
    bb=mazo_falso[int(play_2[1])][int(play_2[0])]
    mazo_falso[int(play_2[1])][int(play_2[0])]=mazo[int(play_2[1])][int(play_2[0])]
    print_mesa(mazo_falso)
    a=mazo_falso[int(play_1[1])][int(play_1[0])]
    b=mazo_falso[int(play_2[1])][int(play_2[0])]
    if a==b:
        puntos+=1
        mazo_falso[int(play_1[1])][int(play_1[0])]=" "
        mazo[int(play_1[1])][int(play_1[0])]=" "
        mazo_falso[int(play_2[1])][int(play_2[0])]=" "
        mazo[int(play_2[1])][int(play_2[0])]=" "
        again="Si"
        return mazo, mazo_falso, puntos, again
    else:
        mazo_falso[int(play_1[1])][int(play_1[0])]=aa
        mazo[int(play_1[1])][int(play_1[0])]=a
        mazo_falso[int(play_2[1])][int(play_2[0])]=bb
        mazo[int(play_2[1])][int(play_2[0])]=b
        again="No"
        return mazo, mazo_falso, puntos, again

    

cartas=int(input("Inserte mazo:"))

mazo=[]
mazo_falso=[]
for a in range(cartas):
    mazo.append(a+1)
    mazo.append(a+1)
    mazo_falso.append("*")
    mazo_falso.append("*")

random.shuffle(mazo)
random.shuffle(mazo_falso)
mazo=generar_matrices((cartas*2),mazo)
mazo_falso=generar_matrices((cartas*2),mazo_falso)


print_mesa(mazo_falso)
print()
game=True
score1=0
score2=0
while game==True:
    
    print("----------")
    a=0
    while a==0:
        
        print("Jugador 1")
        mazo, mazo_falso, score1, again= playing(mazo,mazo_falso,score1)
        if again!="Si":
            print("Jugador 1:" , score1 ,"puntos")
            a=1
            print_mesa(mazo_falso)
            print()
        else:
            print("Jugador 1:" , score1 ,"puntos")
            total=score1+score2
            if total==(cartas):
                game=False
                a=1
            print_mesa(mazo_falso)
            print()
    b=0
    total=score1+score2
    if total==cartas:
        game=False
        b=1
    
    print("----------")
    
    while b==0:
        print("Jugador 2")
        mazo, mazo_falso, score2, again= playing(mazo,mazo_falso,score2)
        if again!="Si":
            b=1
            print("Jugador 2:" , score2 ,"puntos")
            print_mesa(mazo_falso)
            print()
        else:
            print("Jugador 2:" , score2 ,"puntos")
            total=score1+score2
            if total==(cartas):
                game=False
                b=1
            print_mesa(mazo_falso)
            print()
    
        




if score1>score2:
    print("Ganó el jugador 1")

elif score1<score2:
    print("Ganó el jugador 2")

else:
    print("Empate")


    
