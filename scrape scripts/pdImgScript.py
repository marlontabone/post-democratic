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

for x in range(88272,97967): #2017 blogs range

    #url we are using for our webscrape
    my_url = "https://daphnecaruanagalizia.com/?p=" + str(x)

    try:
        r = requests.get(my_url) #sending a request to the above url

    except requests.exceptions.RequestException as e:    # This is the correct syntax
    #if page was not found program skips
        print("skipping this one")
        print(e)
        sys.exit(1)

    page = soup((r.content),"html.parser") #parse recevied content as an html object using BS
    content = page.find("div",{"class":"entry"}) #look for a div classed as entry

    if content is not None: #if div class entry exists then look for tag p of class none in it
        children = content.findChildren("p",{"class":None},recursive = False)
        if children is not None: #provided there are some p tags continue the below
                for child in children:
                    #search for img tages in the found p tags which have a jpg extension
                    image = child.find('img', {'src':re.compile('.jpg')})
                    if image is not None:
                        #if any images are found request the src
                        image_url = image['src']
                        img = Image.open(requests.get(image_url, stream = True).raw) #open src to get that image
                        index = str(rand.randrange(1,87)) #indexing our images
                        img.save("images/"+index+'.jpg') #saving our images
                        print("saved image") #confirming an image has been saved
