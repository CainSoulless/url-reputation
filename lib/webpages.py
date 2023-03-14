# Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC

# Utils
from lib.utils import get_report_dir_info
from lib.utils import resources

import os
import time 


def ibm_xforce(target, driver):
    print("[*] IBM X-force, creando screenshot.")

    report_folder = get_report_dir_info(target)
    screenshot_dir_name = os.path.join(report_folder["report_folder"], "ibm_xforce.png")
    resource = resources(target)

    driver.get(resource[0][0])

    boton1 = driver.find_element(by=By.ID, value="termsCheckbox")
    boton1.click()
    boton2 = driver.find_element(by=By.CLASS_NAME, value="guestlogin")
    boton2.click()

    try:
        element = driver.find_element(By.CLASS_NAME, value=resource[0][1])
        element.screenshot(screenshot_dir_name)
        print("[+] Screenshot creado con exito.\n")
    except:
        # Omited raise Exception 
        print("[-] Error al crear screenshot.\n")
    

# TODO: Find the way to just screeshot the 'report' id of the DOM tree.
def virus_total(target, driver):
    print("[*] VirusTotal, creando screenshot.")

    report_folder = get_report_dir_info(target)
    screenshot_dir_name = os.path.join(report_folder["report_folder"], "virus_total.png")
    resource = resources(target)

    try:
        driver.get(resource[1][0])
        time.sleep(2)
        driver.save_screenshot(screenshot_dir_name)
        print("[+] Screenshot creado con exito.\n")
    except:
        print("[-] Error al crear screenshot.\n")


def abuseIPDB(target, driver):
    print("[*] abuseIPDB, creando screenshot.")

    report_folder = get_report_dir_info(target)
    screenshot_dir_name = os.path.join(report_folder["report_folder"], "abuseipdb.png")
    resource = resources(target)

    driver.get(resource[2][0])

    element = driver.find_element(By.CLASS_NAME, value=resource[2][1])
    element.screenshot(screenshot_dir_name)

    print("[+] Screenshot creado con exito.\n")