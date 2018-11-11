from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime

driver = webdriver.Firefox()

def inception_finder(url):
    
    url = url + '/about'

    driver.get(url)

    print("Retrieving Inception of:",url)
    months = {'Jan':'01' ,'Feb':'02' ,'Mar':'03' ,'Apr':'04' ,'May':'05' ,'Jun':'06' ,'Jul':'07' ,'Aug':'08' ,'Sep':'09' ,'Oct':'10' ,'Nov':'11'  ,'Dec':'12' }
    inception = driver.find_element(By.XPATH , '//*[@id="right-column"]/yt-formatted-string[2]')
    segments = inception.text.split()
    final_format = segments[3] + '-' + months[segments[1]] + '-' + segments[2][:-1]
    return(final_format)

if __name__ == '__main__' :
    print(inception_finder('https://www.youtube.com/user/LinusTechTips'))