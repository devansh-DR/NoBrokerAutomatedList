from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

FORM_LINK = "YOUR GOOGLE FORM URL"

URL = "YOUR NO BROKER URL AFTER APPLYING ALL THE FILTERS"
response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")

all_flats = soup.find_all(name="a", class_="overflow-hidden")

Flat_description = [flat.text for flat in all_flats]
Flat_link = [f"nobroker.in{flat.get('href')}" for flat in all_flats]

options = Options()
options.set_preference('geo.prompt.testing', True)
driver = webdriver.Firefox(options=options)
driver.get(FORM_LINK)
time.sleep(3)

for n in range(len(Flat_link)):
    # link and description input
    description_input = driver.find_element(By.XPATH,
                                            'COPY XPATH FROM FORM DESCRIPTION INPUT OF GOOGLE FORM')
    description_input.send_keys(Flat_description[n])

    Link_input = driver.find_element(By.XPATH,
                                     "COPY XPATH FROM FORM LINK INPUT OF GOOGLE FORM")
    Link_input.send_keys(Flat_link[n])

    time.sleep(1)
    # submit button
    submit_button = driver.find_element(By.XPATH, "COPY XPATH FROM SUBMIT BUTTON")
    submit_button.click()

    time.sleep(1)
    # submite another form button
    submit_another_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another_button.click()
