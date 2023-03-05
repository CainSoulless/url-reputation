from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options, executable_path=r'/snap/bin/geckodriver')
driver.get("http://google.com/")
driver.save_screenshot("/tmp/screen.png")

print ("Headless Firefox Initialized")
driver.quit()
