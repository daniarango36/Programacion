import concurrent.futures
import time 
import requests
import pandas as pd
# from factorial import operacion as factorial
from weather import funtions



ciudades=['london','paris','tokyo','new york','sydney','moscow','cairo','beijing','mumbai','rio de janeiro']
temps=['max','min']
headers = {
    'Authorization': 'Bearer secret-token-1234'
}
years=10

df=funtions.get_df(ciudades,temps,years,headers)
if __name__ == "__main__":
    df3=funtions.main(df,ciudades,temps,years)
df3.to_excel('resultado.xlsx', index=False)