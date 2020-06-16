#importing beautiful soup 4
import bs4
import requests
import random as rand

from PIL import Image
import string
#we will refer to Beautiful Soup as soup.
from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq
from urllib.request import Request
import re

blogposts = " "

for x in range(88272,97967):

    #url we are using for our webscrape
    my_url = "https://daphnecaruanagalizia.com/?p=" + str(x)

    try:
        r = requests.get(my_url)

    except requests.exceptions.RequestException as e:    # This is the correct syntax
        print("skipping this one")
        print(e)
        sys.exit(1)

    page = soup((r.content),"html.parser")
    content = page.find("div",{"class":"entry"})

    if content is not None:
        children = content.findChildren("p",{"class":None},recursive = False)
        if children is not None:
                for child in children:
                    image = child.find('img', {'src':re.compile('.jpg')})
                    if image is not None:
                        image_url = image['src']
                        img = Image.open(requests.get(image_url, stream = True).raw)
                        index = str(rand.randrange(0,10000))
                        img.save("images/"+index+'.jpg')
                        print("saved image")
