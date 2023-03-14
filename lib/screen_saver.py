# selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# webpages
from lib.webpages import ibm_xforce
from lib.webpages import virus_total 
from lib.webpages import abuseIPDB 

# webdriver-manager
from webdriver_manager.firefox import GeckoDriverManager

# Utils
from lib.utils import open_folder

import os


def get_screeshots(target):
    geckodriver_dir = os.getcwd() + "\\config\\geckodriver\\geckodriver.exe"
    firefox_binary = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    firefox_option = webdriver.FirefoxOptions()
    firefox_option.binary_location = firefox_binary
    firefox_option.add_argument("--headless")

    service = Service(geckodriver_dir)

    driver = webdriver.Firefox(service=service, options=firefox_option)

    abuseIPDB(target, driver)
    ibm_xforce(target, driver)
    virus_total(target, driver)
    open_folder(target)

    service.stop()
    driver.quit()