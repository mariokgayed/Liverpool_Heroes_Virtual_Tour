from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

DRIVER_PATH = 'C:\\Users\\mario\\Desktop\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.maximize_window()
driver.get('https://www.liverpoolfc.com/')

element_to_hover_over = driver.find_element_by_link_text('CLUB')
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
history_link = driver.find_element_by_link_text('HISTORY')
history_link.click()

heroes = driver.find_element_by_xpath('//*[@id="cms-block-19397"]/div/a/h2')
heroes.click()

#players = []
for button in range(10):
    #navigate to the Nth player info page
    players_button = driver.find_elements_by_class_name('btn-circle')
    ActionChains(driver).double_click(players_button[button]).perform()

    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, 1):
        driver.execute_script("window.scrollTo(0, {});".format(i))

    '''#extract the desired info for each player (ex. name, goals, etc..)
    first_name = driver.find_element_by_xpath('.//*[@id="cms-block-19283"]/div/div/div/h1/span[1]').text
    last_name = driver.find_element_by_xpath('.//*[@id="cms-block-19283"]/div/div/div/h1/span[2]').text
    player_name = first_name + ' ' + last_name
    games = driver.find_element_by_xpath('.//*[@id="cms-block-19284"]/div/div[2]/div[1]/span[2]').text
    goals =driver.find_element_by_xpath('.//*[@id="cms-block-19284"]/div/div[2]/div[2]/span[2]').text
    leagues =driver.find_element_by_xpath('.//*[@id="cms-block-19514"]/div/div[1]/span[2]').text
    cups =driver.find_element_by_xpath('.//*[@id="cms-block-19514"]/div/div[2]/span[2]').text
    champions_leagues =driver.find_element_by_xpath('.//*[@id="cms-block-19514"]/div/div[4]/span[2]').text

    create a row with the player's info and append them to 'players' list
    row = [player_name, games, goals,leagues, cups, champions_leagues]
    players.append(row)
    print(players[index])'''

    #go back to players page
    driver.find_element_by_class_name('btn-rect').click()

driver.quit()

