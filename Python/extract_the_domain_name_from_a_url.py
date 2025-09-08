# my sol
def domain_name(url):
    url = url.replace("http://","").replace("https://","").replace("www.","")
    return url.split(".")[0]

# pythonic
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
