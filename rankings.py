import pandas as pd
import bs4
import requests

url = 'https://www.ufc.com/rankings'
resp = requests.get(url)
soup = bs4.BeautifulSoup(resp.content, 'html.parser')


def get_rankings():

    divisions = pd.read_html(url)
    for division in divisions:
        division.columns = ['Rank', 'Fighter', 'Change']
        division.fillna('', inplace=True)

    champions = soup.select('table.cols-0')[0:13]
    for champ, division in zip(champions, divisions):
        try:
            division.loc[-1] = ['Champion', champ.h5.text.strip("\n"), ' ']
            division.index = division.index + 1
            division.sort_index(inplace=True)

        except:
            division.loc[-1] = ['Champion', 'Vacant', ' ']
            division.index = division.index + 1
            division.sort_index(inplace=True)

    p4p, fly, bantam, feather, light, welter, middle, lheavy, heavy = divisions[0:9]  # men's divisions including P4P
    w_p4p, w_straw, w_fly, w_bantam = divisions[9:13]  # women's division including P4P, excluding Women's Featherweight

    p4p = p4p.replace('Champion', '1')
    w_p4p = w_p4p.replace('Champion', '1')


get_rankings()