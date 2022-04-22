import requests, bs4, pandas as pd, pprint as pp

url = 'https://www.ufc.com/rankings'
resp = requests.get(url)
soup = bs4.BeautifulSoup(resp.text, 'html.parser')
df_list = pd.read_html(url)

def rankings_data():

    for i in df_list:
        i.columns = ['Rank', 'Fighter', 'Change']
        i.fillna('', inplace= True)

    p4p, fly, bantam, feather, light, welter, middle, lheavy, heavy = df_list[0:9] #men's divisions including P4P
    w_p4p, w_straw, w_fly, w_bantam= df_list[9:13] #women's division including P4P, excluding Women's Featherweight because there are no contenders

    # Work in progress
    for champ in soup.select('div.rankings--athlete--champion')[0:13]:
        x = map(champ.h5.text,i)

        pp.pprint(x)

rankings_data()
