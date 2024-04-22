import random as rd
direcciones = [(0,1),(-1,0),(0,-1),(0,1),(1,1),(-1,1),(1,-1),(-1,-1)]
bola = [2,2]
tablero = [
    ["|","_","_","_","_","|"],
    ["|","_","_","_","_","|"],
    ["|","_","_","_","_","|"],
    ["|","_","_","_","_","|"],
    ["|","_","_","_","_","|"],
    ["|","_","_","_","_","|"],
]

def imprimirTablero():
    tablero[bola[0]][bola[1]]= "B"
    
    for x in range(6):
        print(tablero[x])
    tablero[bola[0]][bola[1]]="_"
    print()
    
def jugada():
    while True:
        direccion = rd.choice(direcciones)
        bola[0]+= direccion[0]
        bola[1]+= direccion[1]
        if bola[0]<1 or bola[1]<1 or bola[0]>5 or bola[1]>5:#salida del tablero
            print("Perdiste")
            break
        if tablero[bola[0]][bola[1]]=="|": #comprobarpared
            bola[0]-= direccion[0]
            bola[1]-= direccion[1]
            continue
        
while True:
    jugada()
    imprimirTablero()
    
