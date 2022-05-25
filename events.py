from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import bs4
import requests

url = 'https://www.ufc.com/events#events-list-past/'

resp = requests.get(url)
soup = bs4.BeautifulSoup(resp.content, 'html.parser')

driver = webdriver.Edge()
driver.get(url)
driver.implicitly_wait(0.5)

event_cards = driver.find_elements(by=By.CLASS_NAME, value='l-listing__item')

for event_card in event_cards:
    event_link = driver.find_elements(by=By.XPATH, value='//*[@id="events-list-past"]/div/div/div[2]/div/div/section/ul/li[1]/article/div[1]/div/a')


driver.find_element(
    by=By.XPATH,
    value='//*[@id="events-list-past"]/div/div/ul/li/a').\
    send_keys("webdriver" + Keys.ENTER)


# driver.quit()