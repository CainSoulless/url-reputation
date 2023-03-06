from utils import resources

from selenium import webdriver
from selenium.webdriver.common.by import By 

def ibm_xforce(target, driver):
    resource = resources(target)
    driver.get(resource[0][0])

    boton1 = driver.find_element(by=By.ID, value="termsCheckbox")
    boton1.click()
    boton2 = driver.find_element(by=By.CLASS_NAME, value="guestlogin")
    boton2.click()

    element = driver.find_element(By.CLASS_NAME, value=resource[0][1])
    element.screenshot(f"screen1.png")