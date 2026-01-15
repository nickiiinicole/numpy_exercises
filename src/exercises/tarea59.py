import numpy as np

arr1= np.arange(0,10)
arr2 = np.arange(1, 11)
print(f"{arr2}")

arr3 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"Odd numbers {arr3[arr3%2==0]}")

arr4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr4[arr4%2!=0]=0

print(f"Change for zeros: {arr4}")

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

# acordarse de los axis = 0 -> vertical filas
print(f"{np.concatenate((b,a), axis=0)} \n")

print(f"{np.concatenate((a,b), axis=1)}")

#/TODO print(np.vstack((a, b))) probar esa funcionesq hacen lo = 
#/TODO print(np.hstack((a, b)))