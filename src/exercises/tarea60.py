import numpy as np
import pandas as pd

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
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
# pair_max(a, b)
# # #> array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])

# La vectorización es, básicamente, 
# eliminar los bucles for de Python 
# y empujar ese trabajo a una capa inferior 
# mucho más rápida (escrita en C).

# Usar np.vectorize , es como un adaptador que coge los arrays en este caso 
# a y b y los recorre elemento a elemento y te va pasando los numeros 
# entonces haces ahi la condicion
# Esto crea una nueva función 'pair_max' que internamente hace el bucle por ti
pair_max = np.vectorize(maxx)

resultado = pair_max(a, b)

print("Array A:", a)
print("Array B:", b)
print("Máximos:", resultado)

# otra manera de hacerlo es :
pair_max = np.frompyfunc(maxx, 2, 1)
result = pair_max(a, b)
result_parseado = result.astype(int)

print("Array A:", a)
print("Array B:", b)
print("Máximos:", result_parseado)

columnas = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

try: 

    df_iris= pd.read_csv("./resource/iris.data", names=columnas)
    sepal_length = df_iris['sepal_length'].to_numpy()
    print(df_iris['sepal_length'])

    minimo = sepal_length.min()  
    maximo = sepal_length.max()  
    rango = maximo - minimo

    
    sepal_normalizado = (sepal_length - minimo) / rango
    print(sepal_normalizado[:5])

except Exception as e:
    print(f"Error: {e}")