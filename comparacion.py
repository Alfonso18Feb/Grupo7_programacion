import os
'''
La funcion que permite comparar las notas de lucia y carlos
'''
def compareTriplets(a, b):
    carlos_score = 0
    lucia_score = 0

    for i in range(len(a)):
        #el rango es la longitud de la lista a
        if a[i] > b[i]:
            lucia_score += 1
             #compara y añade un punto a lucia
        elif a[i] < b[i]:
            carlos_score += 1
            #compara y añade un punto a carlos
        else:
            lucia_score and carlos_score ==0
            #no añade puntos

    return [lucia_score, carlos_score] #devuelve el resultado de lucia y carlos
'''
Aqui se crean las listas a y b (a lista lucia y b de carlos) y tiene una excepción si escribes mal las lista
'''
if __name__ == '__main__':
    # Cambia el nombre del archivo de salida según tus necesidades
    output_file_path = "output.txt"

    try:
        # Solicitar al usuario que ingrese números y manejar casos de entrada no válidos
        a = list(map(int, input("Ingrese los valores de la lista 'a': ").rstrip().split()))
        b = list(map(int, input("Ingrese los valores de la lista 'b': ").rstrip().split()))
    except ValueError:
        print("Error: Ingrese solo números válidos.")
        exit()
    print(compareTriplets(a, b))
