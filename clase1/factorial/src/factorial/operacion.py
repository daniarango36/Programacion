import math
from scipy import stats
import statistics
import numpy as np

def multiplicar(a,b):
    resultado=a*b
    return resultado

def restar(a,b):
    resultado=a-b
    return resultado

def factorial(a):
    for i in range(a+1):
        if i==0:
            b=1
        else:
            b=b*i
    return b

def promedio(df):
    if not isinstance(df, list) or all(isinstance(item, (int, float)) for item in df)==False:
        print("Debe ser una lista")
    else:
        promedio = sum(df) / len(df)
    return promedio

def mediana(df):
    if not isinstance(df, list) or all(isinstance(item, (int, float)) for item in df)==False:
        print("Debe ser una lista")
    else:
        mediana = statistics.median(df)
    return mediana

def moda(df):
    if not isinstance(df, list) or all(isinstance(item, (int, float)) for item in df)==False:
        print("Debe ser una lista")
    else:
        moda = statistics.mode(df)
    return moda

def varianza(df):
    if not isinstance(df, list) or all(isinstance(item, (int, float)) for item in df)==False:
        print("Debe ser una lista")
    else:
        varianza = statistics.variance(df)
    return varianza

def desviacion(df):
    if not isinstance(df, list) or all(isinstance(item, (int, float)) for item in df)==False:
        print("Debe ser una lista")
    else:
        desviacion = statistics.stdev(df)
    return desviacion

def pesoposicional(df,df1):
    if not isinstance(df, list) or all(isinstance(item, (int, float)) for item in df)==False:
        print("Debe ser una lista")
    else:
        pesoposicional = stats.weightedtau(df,df1)
    return pesoposicional
