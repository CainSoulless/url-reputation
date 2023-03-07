# webdriver-manager
from webdriver_manager.firefox import GeckoDriverManager

import os

from selenium import webdriver

def check_geckodriver_installation():
    if not os.path.exists("/snap/bin/geckodriver"):
        webdriver.Firefox(executable_path=GeckoDriverManager().install())
