import random as rd
direcciones = [(1,0),(-1,0),(0,-1),(0,1)]
fantasma = []
pacman = [4,4]
tablero = [
    ["_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_"],
]
def generarFantasmas():
    for i in range(4):
        numx= rd.randint(0,7)
        numy= rd.randint(0,7)
        fantis = [numx,numy]
        if numx == 4 and numy == 4:
            continue
        for j in range (len(fantasma)):
            if fantasma[j] == fantis:
                continue 
        fantasma.append([numx,numy])
        print(fantasma)

generarFantasmas()
def imprimirTablero():
    tablero[pacman[0]][pacman[1]]="🟡"
    for i in range(len(fantasma)):
        tablero[fantasma[i][0]][fantasma[i][1]]="👻"
    for x in range(8):
        print(tablero[x])
    tablero[pacman[0]][pacman[1]]="_"
    print()

def jugada():
    while True:
        movimiento = rd.choice(direcciones)
        pacman[0]+=movimiento[0]
        pacman[1]+=movimiento[1]
        if pacman[0]<0 or pacman[1]<0 or pacman[0]>7 or pacman[1]>7:
            pacman[0]-=movimiento[0]
            pacman[1]-=movimiento[1]
            continue
        else:
            break
    if tablero[pacman[0]][pacman[1]] == "F":
        print("Peldiste tontis")

while True:
    jugada()
    imprimirTablero()
    if pacman in fantasma:
        break