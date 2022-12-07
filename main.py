# IMPORT NECCESSARY LIB
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.date import now
from utils.macenaries import scrape as macenaries_scrapper
from utils.battlegrounds import scrape as battlegrounds_scrapper
from utils.cards import scrape as cards_scrapper
from utils.pil_bg import convert_bg



# CONFIG FOR PRODUCTION ENV
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)


# driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
# driver = webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()), options=chrome_options)         


while True:
    print('Scraping 1...........................', now())
    macenaries_scrapper(webdriver, Service, chrome_options, WebDriverWait, By, EC)
    time.sleep(5)


# print('Scraping 2...........................', now())
# cardbacks_scrapper(webdriver, Service, chrome_options, WebDriverWait, By, EC)
# time.sleep(5)


# print('Scraping 3...........................', now())
# battlegrounds_scrapper(webdriver, Service, chrome_options, WebDriverWait, By, EC)
# time.sleep(5)


# print('Scraping 4...........................', now())
# cards_scrapper(webdriver, Service, chrome_options, WebDriverWait, By, EC)

# convert_bg()    


