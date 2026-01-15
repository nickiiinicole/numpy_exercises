import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
#Obten os elementos que se encontran en a e en b na mesma posicion.
matches = a[a==b]
print(matches)
# Obten todos os numeros do array a que se encontren entre 5 e 10
a = np.array([2, 6, 1, 9, 10, 3, 27])

print(a[(a>=5) & (a<=10)])

# Sexa a función maxx definida como:
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y
# Fai que se aplique de xeito vectorial de tal xeito 
# que se o aplicamos aos array a e b obteñamos o seguinte resultado.
# a = np.array([5, 7, 9, 8, 6, 4, 5])
# b = np.array([6, 3, 4, 8, 9, 7, 1])
# pair_max(a, b)
# #> array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])
