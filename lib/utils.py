# urllib
import urllib.parse

# filenaming
import datetime

import os


def resources(target):
    url = url_encode(target)
  
    resources_list = [
        ["https://exchange.xforce.ibmcloud.com/url/" + url, "instantresultwrapper"],
        ["https://www.virustotal.com/gui/search/" + url, "report"],
        ["https://urlscan.io/search/"]
    ]

    return resources_list


def url_encode(target):
    url_encoded = urllib.parse.quote_plus(target)

    return url_encoded


def get_report_name_creator(target):
    # Just traverse the string and replace all dot for prevent
    # problems.
    target = target.replace('.', '')

    now = datetime.datetime.now()
    actual_hour = now.strftime("%H-%M")
    actual_day = now.strftime("%d-%m")
    
    filename = f"{target}_{actual_hour}_{actual_day}"

    return filename 


def get_report_dir_info(target):
    report_dir = os.path.join(os.getcwd(), "reports")
    folder_name = get_report_name_creator(target)
    report_folder = os.path.join(report_dir, folder_name)
    report_filename_txt = os.path.join(report_folder, f"{target}.txt")

    return {
            "report_dir": report_dir,
            "folder_name": folder_name,
            "report_folder": report_folder,
            "report_filename_txt": report_filename_txt
    }


def open_folder(target):
    report_dir_info = get_report_dir_info(target)
    report_dir_info = report_dir_info["report_dir"]
    folder_list = sorted(os.listdir(report_dir_info), key=lambda carpeta: 
                         os.stat(os.path.join(report_dir_info, carpeta)).st_ctime, 
                         reverse=True)

    latest_folder = os.path.join(report_dir_info, folder_list[0])
    os.startfile(latest_folder)