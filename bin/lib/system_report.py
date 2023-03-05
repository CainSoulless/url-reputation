# API 
import requests

# filenaming
from datetime import date

import os

def filename_creator(target):
    datetime = date.today()
    filename = f"{str(target)}-{datetime}.txt"

    return filename 


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
    filename = filename_creator(target)
    report_body = api_id(target)

    with open(f"..\\reports\\{filename}", "w") as f:
        f.write(report_body)