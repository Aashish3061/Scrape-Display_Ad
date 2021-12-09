from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

from bs4 import BeautifulSoup

from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

s = Service(r"C:\Users\aasis\Downloads\chromedriver_win32\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://www.speedtest.net/")

browser.switch_to.frame("google_ads_iframe_\/6692\/speedtest\.net\/stnext_bottom_rectangle_0")

browser.switch_to.frame("google_ads_iframe_\/22360841743\,6692\/AAXB54Y5G_334220104-AAX_0")

page_source=browser.page_source
soup = BeautifulSoup(page_source, 'lxml')

ad_img=browser.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/a/amp-img/img")
with open('Image.png', 'wb') as file:
  file.write(ad_img.screenshot_as_png)

ad_ti=soup.find_all("a", class_=re.compile("title"))
print(ad_ti.string)

ad_log=browser.find_elements_by_xpath("/html/body/div[1]/div/div/div[4]/a")
with open('Logo.png', 'wb') as file1:
  file1.write(ad_log.screenshot_as_png)

ad_adv=soup.find_all("a", class_=re.compile("advertiser"))
print(ad_adv.string)

ad_cta=soup.find_all("a", class_=re.compile("call-to-action"))
print(ad_cta.string)

browser.quit()
