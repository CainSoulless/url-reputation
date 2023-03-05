# selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By 

from utils import resources
from utils import url_encode 


def get_screeshots(target):
    firefox_option = Options()
    firefox_option.add_argument("--headless")
    service = Service("/snap/bin/geckodriver")

    driver = webdriver.Firefox(service=service, options=firefox_option)


    driver.quit()
    resources = resources()

    for i, resource in enumerate(resources):
        payload = resource + url_encode(target)
        driver.get(payload)
        element = driver.find_element(By.CLASS_NAME, value=resource[1])
        element.screenshot("/tmp/screen{1}.png")
