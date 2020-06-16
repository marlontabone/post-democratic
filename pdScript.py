#importing beautiful soup 4
import bs4
import requests
#we will refer to Beautiful Soup as soup.
from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq
from urllib.request import Request

blogposts = " "

for x in range(93661,97967):

    #url we are using for our webscrape
    my_url = "https://daphnecaruanagalizia.com/?p=" + str(x)

    try:
        r = requests.get(my_url)

    except requests.exceptions.RequestException as e:    # This is the correct syntax
        print("skipping this one")
        print(e)
        sys.exit(1)

    page = soup((r.content),"html.parser")

    text = page.find("div", {"class":"entry"})

    if text is not None:
        children = text.findChildren("p",{"class":None}, recursive=False)
        if children is not None:
            for child in children:
                actual = child.get_text()
                #print(actual)
                file  = open('1.txt','a')
                file.write(actual)
                file.close()
                print(x)
