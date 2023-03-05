import webbrowser as wb
import os

# lib
from lib.system_report import report_creator
from lib.utils import resources

# utils
from lib.utils import url_encode

def browser_starter():
    """
    Check which operative system are running, and then determine
    the browser path. 
    """
    operative_system_name = os.name
    linux_firefox_dirs = [
        "/snap/bin/firefox",
        "usr/bin/firefox"
    ]

    if operative_system_name == "nt":
        firefox = wb.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        return firefox

    for dir in linux_firefox_dirs:
        if os.path.exists(dir):
            firefox = wb.Mozilla("/snap/bin/firefox")
            break

    return firefox


def webpages_open(target):
    """
    Opens  all the webpages previously implemented, with the url/ip 
    required by the operator.
    """
    resourses = resources()

    browser = browser_starter()

    for resourse in resourses:
        payload = resourse + url_encode(target)
        browser.open(payload)


# TODO: Delete after production software.
def debug():
    url = "https://www.urlencoder.io/python/"

    print(f"After: {url}")
    print(f"Before: ", end="")
    print(url_encode(url)) 