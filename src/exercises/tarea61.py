import pandas as pd 
import numpy as np 

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
try:
    df_iris = pd.read_csv("./resource/iris.data", names=columns)

    print(df_iris['class'].unique())
    # .cat.codes asigna automaticamente 0, 1, 2... a cada categoría única atopada.
    df_iris['class_num'] = df_iris['class'].astype('category').cat.codes

    valores_unicos = df_iris['class'].unique()
    print(f"\nClases únicas: {valores_unicos}")

    # 4. Asignar valor numérico automático
    # O xeito máis potente en Pandas é usar o tipo 'category'.
    # .cat.codes asigna automaticamente 0, 1, 2... a cada categoría única atopada.
    df_iris['class_num'] = df_iris['class'].astype('category').cat.codes

    print("\n--- Resultado con nova columna numérica ---")
    # Mostramos unha mostra aleatoria para ver as diferentes clases
    print(df_iris[['class', 'class_num']].sample(10))

    # OPCIONAL: Se queres ver que número se asignou a que texto:
    # Creamos un dicionario para comprobar
    mapeo = dict(enumerate(df_iris['class'].astype('category').cat.categories))
    print(f"\nMapeo automático realizado: {mapeo}")

except Exception as e:
    print(f"Erro: {e}")