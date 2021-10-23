import math
import sys

try:
    result=math.factorial(2.4)
except:
    print('Error inesperado.',sys.exc_info()[0])
else:
    print('el factorial es',result)