from config import getApi

api = getApi()

def postStatus(update):

    status = api.PostUpdate(update)
    print(status)

postStatus("Hi, I am a TwitterBot, this my first Tweet.")
