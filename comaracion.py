import os

def compareTriplets(a, b):
    carlos_score = 0
    lucia_score = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            lucia_score += 1
        elif a[i] < b[i]:
            carlos_score += 1
        else:
            lucia_score and carlos_score ==0

    return [lucia_score, carlos_score]

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
    #    with open(output_file_path, 'w') as fptr:
    #        result = print(compareTriplets(a, b))
    #        fptr.write(' '.join(map(str, result)))
    #        fptr.write('\n')
