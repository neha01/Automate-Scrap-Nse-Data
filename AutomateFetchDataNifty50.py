import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import bs4 as bs
import requests

def nifty50_list():
    resp = requests.get('https://en.wikipedia.org/wiki/NIFTY_50')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'},'tbody')
##    print table
    tickers = []
    for row in table.findAll('tr')[1:]:
##        print row
        ticker = row.findAll('td')[1].text
        print ticker
        tickers.append(ticker)
        
    with open("nifty50_list.pickle","wb") as f:
        pickle.dump(tickers,f)
        
    return tickers

nifty50_list()



# create a new Chrome session
driver = webdriver.Chrome()
##driver.implicitly_wait(30)
driver.maximize_window()

#Navigate to NSE's(National stock exchange) archive page where historical data of any stock can be downloaded in archive format
driver.get("https://www.nseindia.com/products/content/equities/equities/eq_security.htm")

#Selecting 12 month daterange to fetch the data


with open("nifty50_list.pickle","rb") as f:
            tickers = pickle.load(f)


for ticker in tickers[20:]:
     driver.execute_script("$('#dateRange').val('12month')")
     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'symbol')))
     driver.execute_script("$('#symbol').click()")
     driver.find_element_by_id('symbol').send_keys(ticker)
     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "get"))).click()
     try:
         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@class='download-data-link']/a"))).click()
         
     except:
         print "data not available for {} on NSE for 12 months".format(ticker)
     try:
         WebDriverWait(driver, 3).until(EC.alert_is_present(),'Timed out waiting for alert creation ' +'confirmation alert to appear.')
         alert = driver.switch_to.alert
         alert.accept()
         print("alert accepted")

     except:
         print "No alert"
     
     driver.implicitly_wait(10)
     driver.refresh()


