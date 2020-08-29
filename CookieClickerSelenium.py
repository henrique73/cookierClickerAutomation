from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)

while True:
    driver.find_element_by_xpath("/html/body/div/div[2]/div[15]/div[8]/div[1]").click()
    for i in range(0, 16):
        ProductName = "product" + str(i)
        structureElement = driver.find_element_by_id(ProductName)
        if structureElement.get_attribute("class") == "product unlocked enabled":
            structureElement.click()

    try:
        upgradeElement = driver.find_element_by_id("upgrade0")
        if upgradeElement.get_attribute("class") == "crate upgrade enabled":
            upgradeElement.click()
    except:
        pass

    time.sleep(0.01)


    



