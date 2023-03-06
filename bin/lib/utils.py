# urllib
import urllib.parse

def resources(target):
    url = url_encode(target)
  
    resources_list = [
        ["https://exchange.xforce.ibmcloud.com/url/" + url, "instantresultwrapper"],
        ["https://www.virustotal.com/gui/search/" + url, "container p-4"],
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
