from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver import FirefoxOptions
import re

def webinteraction(username):
   movieList = []

   opts = FirefoxOptions()
   opts.add_argument("--headless")
   driver = webdriver.Firefox(options=opts)

   driver.get("https://letterboxd.samlearner.com/")
   input_element = driver.find_element(By.ID, "mui-1")
   input_element.send_keys(username)

   form = driver.find_element(By.CLASS_NAME, 'recommendation-form')
   button_element = form.find_element(By.CLASS_NAME, 'submit-button')
   button_element.click()
   button_element.click()

   wait = WebDriverWait(driver, timeout = 45)
   wait.until(EC.presence_of_element_located((By.ID, 'download-container')))
   htmlSource = driver.page_source

   soup = BeautifulSoup(htmlSource, 'html.parser')

   for link in soup.find_all(class_="title-link"):
      driver.get(link.get('href'))
      movieSource = driver.page_source
      soup2 = BeautifulSoup(movieSource, 'html.parser')
      content = soup2.find(href = re.compile('themoviedb.org/movie/'))
      idOnly = re.findall(r'\d+', content.get('href'))
      idString = ''.join(idOnly)
      movieList.append(idString)


   driver.quit()
   return movieList

