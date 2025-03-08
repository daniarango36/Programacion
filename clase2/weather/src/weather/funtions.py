import concurrent.futures
import time 
import requests
import pandas as pd
from factorial import operacion as factorial
import asyncio
import multiprocess

def get_data(url, headers,i, city, temp):
    try:
        response = requests.get(url, headers=headers)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON data
            data = response.json()
            # Convert the JSON data to a DataFrame
            df = pd.DataFrame(data)
        else:
            print(f"Failed to retrieve data: {response.status_code} year {i} city {city} temp {temp}")
            df = get_data(url, headers,i, city, temp)  # Return an empty DataFrame in case of failure
    except Exception as e:
        print(f"An error occurred: {e} in this year {i}")
        df = get_data(url, headers,i, city, temp)  # Return an empty DataFrame in case of an exception
    return df

def get_structure(city, temp, i, headers):
    url = f'https://weather.siel.com.co/city/{city}/temp/{temp}'
    df = get_data(url, headers,i, city, temp)
    if not df.empty:
        df['city'] = city
        df['temp'] = temp
        df['year'] = i
        df.rename(columns={df.columns[0]: 'weather'}, inplace=True)
    return df

def get_df(cities, temps, years, headers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        dfs_list = []
        for city in cities:
            for temp in temps:
                for i in range(years):
                    futures.append(executor.submit(get_structure, city, temp, i, headers))
        for future in concurrent.futures.as_completed(futures):
                df = future.result()
                if not df.empty:
                    dfs_list.append(df)
    df = pd.concat(dfs_list)
    return df

def get_information_report(df, city, temp, year):
    dfs_list = []  # Lista para almacenar los DataFrames procesados
    
    
        # Filtrar el DataFrame
    filtered_df = df[(df['city'] == city) & (df['temp'] == temp) & (df['year'] == year)]
        
        # Asegurarse de que el DataFrame filtrado no esté vacío
    if not filtered_df.empty:
            # Calcular promedio y varianza
        avg = factorial.promedio(filtered_df['weather'].tolist())
        var = factorial.varianza(filtered_df['weather'].tolist())
            
            # Crear un nuevo DataFrame con los resultados
        result_df = pd.DataFrame({
            'Average': [avg],
            'Variance': [var],
            'city': [city],
            'temp': [temp],
            'year': [year]
            })
        dfs_list.append(result_df)
    else:
        print(f"No data to display for city: {city}, temp: {temp}, year: {year}")
    
    # Concatenate all the result DataFrames
    final_df = pd.concat(dfs_list, ignore_index=True) if dfs_list else pd.DataFrame()
    return final_df

def main(df, ciudades, temps, years):
    start_time = time.time()
    dfs_list = []  # Lista para almacenar los DataFrames procesados

    # Usamos el ProcessPoolExecutor para ejecutar los trabajos en paralelo
    with multiprocess.Pool() as pool:
        futures = []  # Lista para almacenar los futuros

        # Enviar todas las tareas a los procesos en paralelo
        for ciudad in ciudades:
            for temp in temps:
                for year in range(1, years + 1):  # Asegurarse de que el rango de años comience en 1
                    # Verificar si hay datos para la combinación de ciudad, temp y year
                    if not df[(df['city'] == ciudad) & (df['temp'] == temp) & (df['year'] == year)].empty:
                        futures.append(pool.apply_async(get_information_report, (df, ciudad, temp, year)))
        
        # Recoger los resultados cuando se completen
        for future in futures:
            try:
                result = future.get()  # Obtener el resultado de la tarea
                if not result.empty:
                    dfs_list.append(result)  # Agregar el DataFrame si no está vacío
            except Exception as e:
                print(f"An error occurred: {e}")
    
    # Combinar todos los resultados en un único DataFrame
    if dfs_list:
        final_df = pd.concat(dfs_list, ignore_index=True)
    else:
        print("No data to display")
        final_df = pd.DataFrame()  # Si no hay datos, devolver un DataFrame vacío
    
    print(f"Execution time: {time.time() - start_time} seconds")
    return final_df

