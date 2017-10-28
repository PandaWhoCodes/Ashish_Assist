import urllib.request, random
from PIL import Image
import io
import re
from bs4 import BeautifulSoup


def f(n):
    try:
        page = 'http://xkcd.com/' + n + '/'
        response = urllib.request.urlopen(page)
        text = str(response.read())
        # Now finding the link of the comic on the page
        ls = text.find('embedding')
        le = text.find('<div id="transcript"')
        link = text[ls + 12:le - 2]  # + ".jpg"
        # Now finding the title of the comic
        ts = text.find('ctitle')
        te = text.find('<ul class="comicNav"')
        title = text[ts + 8:te - 8]
        img = title + '.jpg'
        # Now downloading the image
        # print('Now downloading - ' + img)
        print(link, img)
        # urllib.request.urlretrieve(link, img)
        fd = urllib.request.urlopen(link)
        image_file = io.BytesIO(fd.read())
        im = Image.open(image_file)
        im.show()
    except:
        pass


def getNum(link):
    num = ""
    for c in link:
        if c.isdigit():
            num = num + str(c)
    return num


def latest():
    try:
        comic = urllib.request.urlopen("http://xkcd.com")
        # content = comic.text
        content = str(BeautifulSoup(comic.read().decode('utf-8', 'ignore'), "lxml"))
        # Now finding the latest comic number
        ns = content.find('this comic:')
        newstring = content[ns: ns + 40]
        link = re.findall(r'(https?://[^\s]+)', newstring)[0]
        latest = int(getNum(link))
        return int(latest)
    except Exception as e:
        print(e)
        print('Try again later')
        exit()
        return 0


def GetComics():
    val = str(random.randint(1, latest()))
    f(val)
