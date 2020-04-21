#importing beautiful soup 4
import bs4
import requests
#we will refer to Beautiful Soup as soup.
from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq
from urllib.request import Request

blogposts = " "

for x in range(0,97967):

    #url we are using for our webscrape
    my_url = "https://daphnecaruanagalizia.com/?p=" + str(x)

    try:
        r = requests.get(my_url)

    except requests.exceptions.RequestException as e:    # This is the correct syntax
        print("skipping this one")
        print(e)
        sys.exit(1)
    page = soup((r.content),"html.parser")
    blogtext = page.find("div",{"class":"entry"})

    if blogtext is not None:
        actualtext = blogtext.get_text()
        #print out web scrapped text.
        blogposts=blogposts+actualtext
        file  = open('check.txt','a')
        file.write(blogposts)
        file.close()
        print(x)
