# IMPORT NECCESSARY LIB
import os
import time
from utils.date import now        
from utils.formatter import format_description_text
from utils.tweet import tweet
import chromedriver_autoinstaller


path = os.getcwd()
default_media = path + '/blizzard.png'
website = 'https://hearthstone.blizzard.com/en-gb/mercenaries'


def scrape(webdriver, Service, chrome_options, WebDriverWait, By, EC):
    driver = webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()), options=chrome_options)

    driver.get(website)
    wait = WebDriverWait(driver, 30)

    # driver.implicitly_wait(10)

    url = None

    all_cards_link = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='MainCardGrid']/div/div[2]/a")))    #CardbackGridLayout__CardGroupCards-tma7ks-2 gBxxwY
    # all_cards_link = main_cards_container.find_elements(By.XPATH, "//div/div[2]/a")

    print("cards.....", len(all_cards_link))
    
 
    for card in all_cards_link:
        tweeted = False
        print('a.href', card.get_attribute('href'))
        print('pat', path)
        with open(path +"/data/macenaries.txt", 'r') as f:
            if card.get_attribute('href') in f.read():
                tweeted = True   
        if tweeted:
            continue  
        else: 
            with open(path +"/data/macenaries.txt", 'a') as f:
                f.write(card.get_attribute('href') + '\n')
            url = card
            break

    if url == None:
        print('No new card available at the moment', now())        
        driver.quit()
    else:
        scrape_card_info(driver, By, url)
        print('done..............', now())         



def scrape_card_info(driver, By, url):
    card_link = url.get_attribute('href')
    driver.get(card_link)

    card_url = driver.find_element(By.XPATH, '//div[contains(@class, "CardModalContent")]')

    card_img_url = card_url.find_element(By.XPATH, './/div/a/div/div/img').get_attribute('src')
    card_title = card_url.find_element(By.XPATH, './/div[2]/h3').text
    card_description = card_url.find_element(By.XPATH, './/div[2]/p[2]').text

    # print(card_img_url, card_title, card_description, card_link)


    intro = '📢 New card spotted 📢'

    total_len = f"{intro}\n\n⚠️ {card_title}\n\n📅 \n\n🌐 {card_link}"
    print(len(total_len))

    desc = format_description_text(card_description, len(total_len))

    text = f"{intro}\n\n⚠️ {card_title}\n📅 {desc}\n\n🌐 {card_link}"

    print(text)

    # UPLOAD TO TWITTER
    tweet(text, card_img_url)

    print('done..............', now())    
    print('Closing.........................')
    driver.quit()
