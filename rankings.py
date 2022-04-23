import requests, bs4, pandas as pd, pprint as pp

url = 'https://www.ufc.com/rankings'
resp = requests.get(url)
soup = bs4.BeautifulSoup(resp.text, 'html.parser')
divisions = pd.read_html(url)

def rankings_data():

    for division in divisions:
        division.columns = ['Rank', 'Fighter', 'Change']
        division.fillna('', inplace= True)

    champions = []
    for champ in soup.select('div.rankings--athlete--champion')[0:13]:
        champions.append(champ.h5.text.strip("\n"))

    for division, champ in zip(divisions, champions):
        division.loc[-1] = ['Champion/#1', champ, ' ']
        division.index = division.index + 1
        division.sort_index(inplace=True)

    print(divisions[1])

    p4p, fly, bantam, feather, light, welter, middle, lheavy, heavy = divisions[0:9] #men's divisions including P4P
    w_p4p, w_straw, w_fly, w_bantam= divisions[9:13] #women's division including P4P, excluding Women's Featherweight



rankings_data()
