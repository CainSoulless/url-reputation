# API 
import requests

# Utils
from lib.utils import get_report_dir_info

# Natives
import os
import sys

def api_id(target):
    url = "https://www.virustotal.com/api/v3/urls"

    payload = f"url={target}"
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "x-apikey": "6a3e7dfab4a4bcc7b85e0465331b4d67a1e03aa5cbee1bdccfb0eccdac25073c"
    }

    response = requests.post(url, data=payload, headers=headers).json()

    id = response.get("data").get("id")
    link_self = response.get("data").get("links").get("self")

    response = requests.get(link_self, headers=headers)
    report_body = response.text

    return report_body


def report_creator(target):
    report_dir_info = get_report_dir_info(target)
    report_body = api_id(target)
    print("[+] Reporte creado en carpeta :\n \t{}".format(report_dir_info["report_folder"]))

    os.makedirs(report_dir_info["report_folder"], exist_ok=True)

    try:
        with open(report_dir_info["report_filename_txt"], 'w') as f:
            f.write(report_body)
        print("[+] Reporte de texto creado con exito.")
    except:
        raise ValueError("[-] Error creando el reporte de texto.")