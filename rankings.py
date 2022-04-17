import requests, bs4, pandas as pd, pprint as pp

df_list = pd.read_html('https://www.ufc.com/rankings')

p4p, fly, bantam, feather, light, welter, middle, lheavy, heavy = df_list[0:9] #men's divisions including P4P
w_p4p, w_straw, w_fly, w_bantam, w_feather = df_list[10:13] #women's division including P4P
