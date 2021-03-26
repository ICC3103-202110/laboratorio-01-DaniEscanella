import random 
def create_matrix(cards,deck):
    if (cards)>10: 
        columns=10
        c_lines=cartas//10
        if (cards%10)!=0:
            c_lines+=1
    else:
        columns=cards//2
        c_lines=2
    deck_final=[]
    for j in range(c_lines):
        one=[]
        for i in range(columns):
            if len(deck)!=0:
                one.append(deck[0])
                deck.pop(0)
            else:
                one.append(" ")
        deck_final.append(one)
    return deck_final

def print__(deck):
    for k in range(len(deck)):
        coords="   "
        line=" "
        for j in range(len(deck[0])):
            coords+=str(j)+"  "
            line+=str(deck[k][j])+"  "
        if k==0:
            print(coords)
            print(" "+str(k)+line)
            
        elif k>0 and k<11:
            print(" "+str(k)+line)
        else:
            print(str(k)+line)


def playing(deck,deck_false,score):
    play_1=str(input("Elija su primera coordenada: ej: 1,0 "))
    play_1=play_1.split(",")
    aa=deck_false[int(play_1[1])][int(play_1[0])]
    deck_false[int(play_1[1])][int(play_1[0])]=deck[int(play_1[1])][int(play_1[0])]
    print__(deck_false)
    play_2=str(input("Elija su segunda coordenada: "))
    play_2=play_2.split(",")
    bb=deck_false[int(play_2[1])][int(play_2[0])]
    deck_false[int(play_2[1])][int(play_2[0])]=deck[int(play_2[1])][int(play_2[0])]
    print__(deck_false)
    a=deck_false[int(play_1[1])][int(play_1[0])]
    b=deck_false[int(play_2[1])][int(play_2[0])]
    if a==b:
        score+=1
        deck_false[int(play_1[1])][int(play_1[0])]=" "
        deck[int(play_1[1])][int(play_1[0])]=" "
        deck_false[int(play_2[1])][int(play_2[0])]=" "
        deck[int(play_2[1])][int(play_2[0])]=" "
        again="Si"
        return deck, deck_false, score, again
    else:
        deck_false[int(play_1[1])][int(play_1[0])]=aa
        deck[int(play_1[1])][int(play_1[0])]=a
        deck_false[int(play_2[1])][int(play_2[0])]=bb
        deck[int(play_2[1])][int(play_2[0])]=b
        again="No"
        return deck, deck_false, score, again

    

cards=int(input("Inserte mazo:"))

deck=[]
deck_false=[]
for a in range(cards):
    deck.append(a+1)
    deck.append(a+1)
    deck_false.append("*")
    deck_false.append("*")

random.shuffle(deck)
random.shuffle(deck_false)
deck=create_matrix((cards*2),deck)
deck_false=create_matrix(cards*2, deck_false)

print__(deck_false)

print()
game=True
score1=0
score2=0
while game==True:
    
    print("----------")
    a=0
    while a==0:
        
        print("Jugador 1")
        deck, deck_false, score1, again= playing(deck,deck_false,score1)
        if again!="Si":
            print("···Jugador 1:" , score1 ,"puntos···")
            a=1
            print__(deck_false)
            
            print()
        else:
            print("···Jugador 1:" , score1 ,"puntos···")
            total=score1+score2
            if total==(cards):
                game=False
                a=1
            print__(deck_false)
            print()
    b=0
    total=score1+score2
    if total==cards:
        game=False
        b=1
    
    print("----------")
    
    while b==0:
        print("Jugador 2")
        deck, deck_false, score2, again= playing(deck,deck_false,score2)
        if again!="Si":
            b=1
            print("···Jugador 2:" , score2 ,"puntos···")
            print__(deck_false)
            print()
        else:
            print("···Jugador 2:" , score2 ,"puntos···")
            total=score1+score2
            if total==(cards):
                game=False
                b=1
            print__(deck_false)
            
            print()
    
    
if score1>score2:
    print("Ganó el jugador 1")

elif score1<score2:
    print("Ganó el jugador 2")

else:
    print("Empate")

