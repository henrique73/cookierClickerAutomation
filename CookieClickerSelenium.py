from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait  
import time

counter = 0
Count = ""

firefox_profile = webdriver.FirefoxProfile('C:')
driver = webdriver.Firefox(firefox_profile)
cache = driver.application_cache

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)

cookie = driver.find_element_by_xpath("/html/body/div/div[2]/div[15]/div[8]/div[1]")
cookieCount = driver.find_element_by_id("cookies")
upgrade0 = driver.find_element_by_xpath("/html/body/div/div[2]/div[19]/div[3]/div[6]/div[2]")
upgrade1 = driver.find_element_by_xpath("/html/body/div/div[2]/div[19]/div[3]/div[6]/div[3]")

while True:
    rest = (cookieCount.text).split(" c", 1)[0]
    print(rest)
    if counter > 1:
        store0 = driver.find_element_by_xpath("/html/body/div/div[2]/div[19]/div[3]/div[5]/div[1]")
    upgrade0Status = upgrade0.get_attribute("class")
    upgrade1Status = upgrade1.get_attribute("class")
    if counter > 1:
        store0Status = store0.get_attribute("class")
        if store0Status == "crate upgrade enabled":
            store0.click()
    if upgrade0Status == "product unlocked enabled":
        upgrade0.click()
        counter = counter + 1
    if upgrade1Status == "product unlocked enabled":
        upgrade1.click()
        counter = counter + 1
    if int(rest) > 1000:
        upgrade2 = driver.find_element_by_xpath("/html/body/div/div[2]/div[19]/div[3]/div[6]/div[4]")
        upgrade2Status = upgrade2.get_attribute("class")
        if upgrade2Status == "product unlocked enabled":
            upgrade2.click()
    if int(rest) > 12000:
        upgrade3 = driver.find_element_by_xpath("/html/body/div/div[2]/div[19]/div[3]/div[6]/div[5]")
        upgrade3Status = upgrade3.get_attribute("class")
        if upgrade3Status == "product unlocked enabled":
            upgrade2.click()
    if int(rest) > 130000:
        upgrade4 = driver.find_element_by_xpath("/html/body/div/div[2]/div[19]/div[3]/div[6]/div[6]")
        upgrade4Status = upgrade4.get_attribute("class")
        if upgrade4Status == "product unlocked enabled":
            upgrade4.click()
    if int(rest) > 130000:
        upgrade5 = driver.find_element_by_xpath("/html/body/div/div[2]/div[19]/div[3]/div[6]/div[7]")
        upgrade5Status = upgrade5.get_attribute("class")
        if upgrade5Status == "product unlocked enabled":
            upgrade5.click()
    else:
        cookie.click()
    time.sleep(0.01)


