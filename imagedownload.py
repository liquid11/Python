import random
import urllib.request


def download(url):
    name = str(random.randrange(1, 1000))+".jpg"
    urllib.request.urlretrieve("http://www.arlnews.com/uploads/3/8/1/0/38109169/5121906_orig.jpg", name)


download("http://www.arlnews.com/uploads/3/8/1/0/38109169/5121906_orig.jpg")