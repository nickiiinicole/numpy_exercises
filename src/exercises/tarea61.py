import pandas as pd 
import numpy as np 

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
try:
    df_iris = pd.read_csv("./resource/iris.data", names=columns)

    print(df_iris['class'].unique())
    # .cat.codes asigna automaticamente 0, 1, 2... a cada categoría única atopada.
    df_iris['class_num'] = df_iris['class'].astype('category').cat.codes

    valores_unicos = df_iris['class'].unique()
    print(f"\nLas clases unicas : {valores_unicos}")

    #   Asignar valor numérico, para ello se usa category en pandas 
    # .cat.codes asigna automaticamente 0, 1, 2... a cada categoría única atopada.
    df_iris['class_num'] = df_iris['class'].astype('category').cat.codes

    print(df_iris[['class', 'class_num']].sample(10))
    
    class_uniques= df_iris['class'].unique() # creo primero las columnas
    dummies = pd.get_dummies(df_iris['class'], dtype=int)
    final_df= pd.concat([df_iris, dummies], axis=1)
    print(final_df.sample(10))
    
except Exception as e:
    print(f"Error: {e}")