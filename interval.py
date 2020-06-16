from threading import Timer

def set_interval(timer,task):
    isStop = task
    if not isStop:
        Timer(timer, set_interval, [timer, task]).start()
