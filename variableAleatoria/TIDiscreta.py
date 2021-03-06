import pandas as pd
import random

def TIDiscreta(dict_va_frecuencia:dict, cant_va:int):
    if (cant_va <= 0):
        raise Exception("La cantidad de variables aleatorias debe ser mayor a 0")
    list_va = list(dict_va_frecuencia.keys())
    list_frec = list(dict_va_frecuencia.values())
    cant_elementos = sum(list_frec)
    for x in range(len(list_frec)):
        if list_frec[x] <=0:
            raise Exception("Las frecuencias observadas deben ser mayores a 0")
        if x == 0:
            list_frec[x] = list_frec[x] / cant_elementos
        else: 
            list_frec[x] = list_frec[x-1] + list_frec[x] / cant_elementos     

    df = pd.DataFrame(columns = ["Random", "V.A."])
    for x in range(cant_va):
        rand = random.uniform(0,1)
        for x in range(len(list_frec)):
            if rand < list_frec[x] :
                index = x
                break
        df = df.append({
            "Random": rand,
            "V.A.": list_va[index]
        }, ignore_index=True)
    return df