# urllib
import urllib.parse

def resources():
    # resourses = [
    #     {"virustotal" : ["https://www.virustotal.com/gui/search/", "container p-4"]},
    #     {"xforce" : ["https://exchange.xforce.ibmcloud.com/url/", "instantresultwrapper"]},
    #     {"urlscan" : ["https://urlscan.io/search/"]}
    # ]

    resourses = [
        "https://www.virustotal.com/gui/search/",
        "https://exchange.xforce.ibmcloud.com/url/",
        "https://urlscan.io/search/"
    ]

    return resources


def url_encode(target):
    url_encoded = urllib.parse.quote_plus(target)
    return url_encoded