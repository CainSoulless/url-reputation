# selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# webpages
from lib.webpages import ibm_xforce
from lib.webpages import virus_total 

# webdriver-manager
from webdriver_manager.firefox import GeckoDriverManager

# Utils
from lib.utils import open_folder

import os


def get_screeshots(target):
    firefox_option = Options()
    firefox_option.add_argument("--headless")
    # service = Service(GeckoDriverManager().install())
    service = Service("C:\\geckodrive\\geckodrive.exe")

    driver = webdriver.Firefox(service=service, options=firefox_option)

    ibm_xforce(target, driver)
    virus_total(target, driver)
    open_folder(target)

    service.stop()
    driver.quit()