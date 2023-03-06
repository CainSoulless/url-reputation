# selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By 

# webdriver-manager
from webdriver_manager.firefox import GeckoDriverManager

# utils
from utils import resources
from utils import url_encode 

# webpages
from webpages import ibm_xforce

import os


def check_geckodriver_installation():
    if not os.path.exists("/snap/bin/geckodriver"):
        webdriver.Firefox(executable_path=GeckoDriverManager().install())


def get_screeshots(target):
    firefox_option = Options()
    # firefox_option.add_argument("--headless")
    service = Service(GeckoDriverManager().install())

    driver = webdriver.Firefox(service=service, options=firefox_option)
    ibm_xforce(target, driver)


# check_geckodriver_installation()
get_screeshots("google.com")