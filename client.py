import urllib.request

cache = {}

url = "website"

def get_page(url):
    if url in cache:
        webpate = cache[url]
    else:
        print("going to website")
        resp = urllib.request.urlopen(url)
        data = resp.read()
        resp.close()

        cache[url] = data

    return cache[url]