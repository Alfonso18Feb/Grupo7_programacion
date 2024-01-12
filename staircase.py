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
        print(spaces + hashes )

if __name__ == '__main__':
    print('introduce el valor de n :')
    n = int(input().strip())
    staircase(n)
