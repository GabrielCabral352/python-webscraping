import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.nba.com/stats/leaders/?Season=2019-20&SeasonType=Regular%20Season"

option = Options()
option.headless = True
driver = webdriver.chrome()
driver.get(url)
driver.quit()   
# pip install requests2
# pip isntall pandas
# pip install lxml
# pip install beatifulsoup4
