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

# CONFIG FOR PRODUCTION ENV
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)


def run():
    print('Scraping for Macenaries..........................', now())
    macenaries_scrapper(webdriver, Service, chrome_options, WebDriverWait, By, EC)
    time.sleep(5)

    print('Scraping for Battleground...........................', now())
    battlegrounds_scrapper(webdriver, Service, chrome_options, WebDriverWait, By, EC)
    time.sleep(5)


    print('Scraping for Cards..........................', now())
    cards_scrapper(webdriver, Service, chrome_options, WebDriverWait, By, EC)


run()
