import webbrowser
import time


loop = 0

print ("This program started at " + time.ctime())
while loop<3:
    time.sleep(10)
    webbrowser.open("http://youtube.com")
    loop +=1


