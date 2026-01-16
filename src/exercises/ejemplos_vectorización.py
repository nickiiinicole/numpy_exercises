import numpy as np

# ==============================================================================
# 1. INTRODUCIÓN: COMO FUNCIONA A MEMORIA EN NUMPY
# ==============================================================================
"""
Cando se crea un array resérvase a memoria contigua necesaria para almacenar 
todos os seus elementos, aínda que non se lles dea valor inicial.

- As posicións de memoria posteriores ao array seguramente se enchan con outros datos: 
o array non poderá crecer.
- Inserir nun array é complicado (custoso computacionalmente).
- Non faremos operacións con arrays que impliquen ir engadindo elementos.

Diferenza coas listas de Python:
1. Non poden crecer (tamaño fixo).
2. Só poden conter un único tipo de dato (homoxéneos).
3. A gran vantaxe: Son moito máis rápidos e eficientes en memoria.
"""

# ==============================================================================
# 2. CREACIÓN DE ARRAYS (ndarray)
# ==============================================================================
print("\n--- 2. CREACIÓN DE ARRAYS ---")

# O tipo de obxecto principal é 'ndarray'.
# Usamos np.array() sobre calquera iterable (lista, tupla, etc).

# Array 1D (Vector)
arr_1d = np.array([1, 2, 3, 4, 5])
print(f"Array 1D: {arr_1d}")

# Array 2D (Matriz)
# Pártese dunha lista de listas
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array 2D:\n{arr_2d}")

# ==============================================================================
# 3. DIMENSIÓNS E TAMAÑO
# ==============================================================================
print("\n--- 3. DIMENSIÓNS E TAMAÑO ---")

# ndim: Número de dimensións (ex: 1 para vector, 2 para matriz)
# shape: Tamaño de cada dimensión (tupla con filas, columnas, etc.)

print(f"Array: \n{arr_2d}")
print(f"Número de dimensións (ndim): {arr_2d.ndim}") # Imprime 2
print(f"Forma (shape): {arr_2d.shape}")             # Imprime (2, 3) -> 2 filas, 3 columnas

# ==============================================================================
# 4. OUTRAS FORMAS DE CREAR ARRAYS
# ==============================================================================
print("\n--- 4. XERADORES DE ARRAYS ---")

# np.arange(): Similar ao range() de Python pero devolve un ndarray.
# Vantaxe: Xera int32 ou int64 (rango limitado pero rápido) vs int arbitrario de Python.
arr_range = np.arange(5)
print(f"np.arange(5): {arr_range}") # [0 1 2 3 4]

# Zeros e Ones: Enchen o array con 0 ou 1.
arr_zeros = np.zeros(5)       # 1D de 5 elementos
arr_ones = np.ones((5, 3))    # 2D de 5x3

print(f"Zeros (5): {arr_zeros}")
print(f"Ones (5x3):\n{arr_ones}")

# ==============================================================================
# 5. VALORES ALEATORIOS (RANDOM)
# ==============================================================================
print("\n--- 5. RANDOM ---")

# rand: Valores flotantes entre 0 e 1
x_rand = np.random.rand(2, 3) 
print(f"Random float (2x3):\n{x_rand}")

# randint: Enteiros dentro dun rango
# size=(20) crea un array de 20 elementos
x_randint = np.random.randint(10, size=(10)) # Números do 0 ao 9
print(f"Random int (0-9): {x_randint}")

# choice: Elixe valores aleatorios dunha lista dada
x_choice = np.random.choice([1, 2, 3, 4], size=(2, 2))
print(f"Random choice:\n{x_choice}")

# ==============================================================================
# 6. TIPOS DE DATOS (DTYPE)
# ==============================================================================
print("\n--- 6. TIPOS DE DATOS ---")

# Un array contén sempre un único tipo de dato.
print(f"Tipo de dato de arr_1d: {arr_1d.dtype}")

"""
Tipos comúns en NumPy:
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - void (fixed chunk of memory)
"""

# ==============================================================================
# 7. RESHAPE (REMODELAR)
# ==============================================================================
print("\n--- 7. RESHAPE ---")

# Os arrays poden ser multidimensionais, pero a memoria onde se almacenan é lineal.
# Reshape cambia como interpretamos esa memoria lineal sen cambiar os datos.
# Nota: NumPy está feito en C, e en C os arrays gárdanse por filas (row-major).

arr_original = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr_reshaped = arr_original.reshape(4, 3) # Convertemos 12 elementos en 4 filas e 3 columnas

print(f"Orixinal: {arr_original}")
print(f"Reshaped (4x3):\n{arr_reshaped}")

# ==============================================================================
# 8. UFUNCS (UNIVERSAL FUNCTIONS) E VECTORIZACIÓN
# ==============================================================================
print("\n--- 8. UFUNCS E VECTORIZACIÓN ---")

"""
Ufuncs é o acrónimo de Universal Functions.
Utilízanse para facer a vectorización (operar con arrays enteiros sen bucles for).
"""

arr1 = np.array([10, 11, 12])
arr2 = np.array([20, 21, 22])

# Suma vectorizada (elemento a elemento)
newarr = np.add(arr1, arr2)
print(f"Suma vectorizada (add): {newarr}")

# Definir a nosa propia Ufunc con 'frompyfunc'
# Isto converte unha función normal de Python nunha función que "come" arrays.

def funcion_base(x, y):
    """Función simple que suma dous números."""
    return x + y

# frompyfunc(función, num_entradas, num_saidas)
# 2 entradas (x, y)
# 1 saída (o resultado da suma)
myadd = np.frompyfunc(funcion_base, 2, 1)

print("\nUfunc personalizada:")
# Agora podemos pasarlle listas ou arrays enteiros
resultado = myadd([1, 2, 3, 4], [5, 6, 7, 8])
print(resultado)

# NOTA IMPORTANTE:
# As dimensións deben coincidir para operar, salvo que a operación sexa 
# cun escalar (un único número), grazas ao Broadcasting.
print(f"Broadcasting (Array + 1): {arr1 + 1}")