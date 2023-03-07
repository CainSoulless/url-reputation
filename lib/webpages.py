# Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC

# Utils
from lib.utils import get_report_dir_info
from lib.utils import resources

import os


def ibm_xforce(target, driver):
    screenshot_dir_name = os.path.join(report_folder[report_folder], "ibm_xforce.png")
    report_folder = get_report_dir_info(target)
    resource = resources(target)

    print()
    print(screenshot_dir_name)
    print()

    driver.get(resource[0][0])

    boton1 = driver.find_element(by=By.ID, value="termsCheckbox")
    boton1.click()
    boton2 = driver.find_element(by=By.CLASS_NAME, value="guestlogin")
    boton2.click()

    element = driver.find_element(By.CLASS_NAME, value=resource[0][1])
    element.screenshot(screenshot_dir_name)
    

# TODO: Find the way to just screeshot the 'report' id
def virus_total(target, driver):
    report_folder = get_report_dir_info(target)
    resource = resources(target)

    driver.get(resource[1][0])
    driver.save_screenshot(os.path.join(report_folder[report_folder], "virus_total.png"))

