#importing beautiful soup 4
import bs4
import requests
#we will refer to Beautiful Soup as soup.
from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq
from urllib.request import Request

for x in range(88272,97967): #2017 blog posts range

    #url we are using for our webscrape
    my_url = "https://daphnecaruanagalizia.com/?p=" + str(x) #url to request

    try:
        r = requests.get(my_url) #requesting specified url

    except requests.exceptions.RequestException as e:    # This is the correct syntax
    #if url returns a page not found skip this url index
        print("skipping this one")
        print(e)
        sys.exit(1)

    page = soup((r.content),"html.parser") #parse received content into html object

    text = page.find("div", {"class":"entry"}) #look for a div element of class entry

    if text is not None: #provided we find div of class entry look for p tags of class none in it
        children = text.findChildren("p",{"class":None}, recursive=False)
        if children is not None:
            #within each of those p tags of class none get_text
            for child in children:
                actual = child.get_text()
                #print(actual)
                file  = open('1.txt','a') #open the specific text file you will be saving this text to, with the option of appending
                #to not erase prior scraped text everytime this is run
                file.write(actual) #append the actual file with new text
                file.close() #close file
                print(x) #print post-id as confirmation of web-scraping job finished on that url.
