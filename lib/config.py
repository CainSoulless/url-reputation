# webdriver-manager
from webdriver_manager.firefox import GeckoDriverManager

import os 

from selenium import webdriver

def check_geckodriver_installation():
    gecko_linux = "/snap/bin/geckodriver"
    gecko_windows = "C:\\geckodriver\\geckodriver.exe"

    if (not os.path.exists(gecko_linux) or
        not os.path.exists(gecko_windows)):
        webdriver.Firefox(executable_path=GeckoDriverManager().install())