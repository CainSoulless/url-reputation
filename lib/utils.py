# urllib
import urllib.parse

# filenaming
from datetime import date

import os


def resources(target):
    url = url_encode(target)
  
    resources_list = [
        ["https://exchange.xforce.ibmcloud.com/url/" + url, "instantresultwrapper"],
        ["https://www.virustotal.com/gui/search/" + url, "report"],
        ["https://urlscan.io/search/"]
    ]

    # resources_list = [
    #     "https://www.virustotal.com/gui/search/",
    #     "https://exchange.xforce.ibmcloud.com/url/",
    #     "https://urlscan.io/search/"
    # ]

    return resources_list


def url_encode(target):
    url_encoded = urllib.parse.quote_plus(target)
    return url_encoded


def report_name_creator(target):
    datetime = date.today()
    name = f"{str(target)}-{datetime}"

    return name 


def get_report_dir_info(target):
    report_dir = os.path.join(os.getcwd(), "reports")
    folder_name = report_name_creator(target)
    report_folder = os.path.join(report_dir, folder_name)
    report_filename_txt = os.path.join(report_folder, f"{target}.txt")

    return {
            "report_dir": report_dir,
            "folder_name": folder_name,
            "report_folder": report_folder,
            "report_filename_txt": report_filename_txt
    }

get_report_dir_info("google.com")