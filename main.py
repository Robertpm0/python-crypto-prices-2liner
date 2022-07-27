import pandas  as pd
import numpy as np
import requests
# .get data  via  Cryptocompare API --> .json --> data data ---> coin data
# change sequence interval:::::: /v2/histohour --> /v2/histoday  ||  /v2/histominute 
x = requests.get("https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=2000").json()['Data']['Data']
print(x)
#convert to df for ez fun :)
df = pd.DataFrame(x)
print(df)
