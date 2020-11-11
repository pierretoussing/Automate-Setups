from selenium import webdriver
from tkinter import Tk
import os
import re

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()


moodle_url = "https://www.moodle.tum.de/"
notion_path = "Notion"

login = open("login.txt", "r")
username = login.readline()
password = login.readline()

driver = webdriver.Chrome("./chromedriver")
driver.get(moodle_url)
driver.set_window_position(-5,0)
driver.set_window_size(width/2, height)

#Go to register page
driver.find_element_by_link_text("Mit TUM-Kennung").click()

#Enter username
driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[1]/input').send_keys(username)

#Enter passwort
driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[2]/input').send_keys(password)

#Submit login
driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[5]/button').click()

#Open all topics
links = driver.find_elements_by_tag_name("a")
links = [link.get_attribute("href") for link in links]
for link in links:
    print(link)
links = [link for link in links if re.search(r"^https://www.moodle.tum.de/course", link)]
links = list(set(links))
for link in links:
    print(link)

driver.get("https://niessner.github.io/I2DL/")
for link in links:
    driver.execute_script('window.open("{}", "_blank");'.format(link))