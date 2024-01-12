#Importamos las utilidades necesarias para la ejecución del programa

import math
import os
import random
import re
import sys
#Comienza la parte principal (main) del programa
if __name__ == '__main__':
        #Definimos el laberinto indicando el número de filas, colunas y túneles que vamos a poner.
    print("Define el laberinto")
    n = int(input("¿Número de filas?"))
    m = int(input("¿Número de columnas?"))
    k = int(input("¿Número de túneles?"))
    print("Ahora define cada fila escribiendo")
    print("* para mina, # para muro, O para libre")
    print("A para la rana, % para la salida")

    board = [list(input("Describe la fila: ")) for _ in range(n)]
    t_exit = dict()
    
    for kk in range(k):
        i1 = int(input("INICIO fila del túnel: ")) - 1
        j1 = int(input("INICIO columna del túnel: ")) - 1
        i2 = int(input("FINAL fila del túnel: ")) - 1
        j2 = int(input("FINAL columna del túnel: ")) - 1
        t_exit[(i1, j1)] = (i2, j2)
        t_exit[(i2, j2)] = (i1, j1)

    states = [(-1, -1)] # Aquí guardamos todas las posiciones a las que puede moverse la rana.
    state2idx = dict()
    v = [0.0]  # Valores de probabilidad.
    s_init = -1
    transitions = [[(0, 1.0)]] # Valores de los posilbles saltos de la rana.
    
    for i1 in range(n):
        for j1 in range(m):
            x = board[i1][j1]
            if x in ["A", "%", "O"]:
                state2idx[(i1, j1)] = len(states)
                states.append((i1, j1))
            elif x in ["#", "*"]:
                state2idx[(i1, j1)] = 0       
            else:
                assert False, x
        #print (state2idx) print para visualizar el funcionamiento correcto de los datos.
    for i1 in range(n):
        for j1 in range(m):
            x = board[i1][j1]
            state_idx = state2idx[(i1, j1)]
            if x in ["A", "%", "O"]:
                if x == "A":
                    s_init = state_idx
                    v.append(0.0) #Valor cuando no sale la rana estando en su posición inicial.
                elif x == "%":
                    v.append(1.0) #Valor cuando sale la rana.
                    transitions.append([(state_idx, 1.0)])  
                elif x == "O":
                    v.append(0.0) #Valor cuando no sale la rana estando en una casilla libre.
                else:
                    assert False, x
                if x in ["A", "O"]:
                    i2, j2 = t_exit[(i1, j1)] if (i1, j1) in t_exit else (i1, j1)
                    succs = []
                    deaths = 0 #Variable para contabilizar las muertes de la rana.
                    """Desde una posición A (inicial) o O (casilla libre)
                        este (for) evalua los movimientos avanzando la rana
                        una casilla a la derecha (0,1), izquierda(0,-1), 
                        arriba(1,0) o abajo(-1,0)."""
                    for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        i3, j3 = i2 + a, j2 + b
                        if (0 <= i3 < n) and (0 <= j3 < m):
                            y = board[i3][j3]
                            if y in ["A", "%", "O"]:
                                succs.append((i3, j3)) #En el salto ha llegado a la casilla de inicio A, la salida % o una libre O.
                            elif y == "*":
                                deaths += 1 #En el salto ha encontrado una mina y muere.
                    """En este (if) se evalúa las veces que no ha muerto y las que si."""
                    if len(succs) == 0:
                        transitions.append([(0, 1.0)])
                    else:
                        t = [(state2idx[s], 1 / (len(succs) + deaths)) for s in succs]
                        if deaths > 0:
                            t.append((0, deaths / (len(succs) + deaths)))
                        transitions.append(t)
    #print(states) #print de control muestra las posiciones donde no hay muro.
    #print(transitions) #print de control muestra los posibles saltos con su probabilidad.
    while True:
        v_old = v.copy()
        for state in range(len(states)):
            x = 0.0
            for succ, prob in transitions[state]:
                x += v[succ] * prob
            v[state] = x
        keep_going = False
        #for para salir del while
        for state in range(len(states)):
            if abs(v[state] - v_old[state]) > 1e-10:
                keep_going = True
                break
        if not keep_going:
            break
    #Imprimimos el resultado expresando la probilidad de que la rana salga del laberinto.
    print("La probabilidad de que salga la rana es del ",v[s_init]*100," %.")





