import math
import os
import random
import re
import sys


'''
Función que pide el numero de # y te lo devuelve con espacios
'''
def staircase(n):
    print('valor de n :',n )
    for i in range(1, n+1):
        spaces = ' ' * (n - i)
        hashes = '# ' * i
        print(spaces + hashes )  # hace un print de las dos variables spaces y hashes
'''
Esta función busca cuantas n# quiere el usuario que el programa escriba
'''
if __name__ == '__main__':
    print('introduce el valor de n :')
    n = int(input().strip())
    staircase(n)
