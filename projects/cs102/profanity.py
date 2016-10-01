import urllib
#profanity script

#Steps
##1. define profanity
##2. get string
##3. check for profanity in string
##4. print warning if yes

def read_text(f):
    words = open(f)
    contents = words.read()
    words.close()
##    print contents
    check_prof(contents)

def check_prof(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
##    print output
    connection.close()
    if "true" in output:
        print ("FUCK FUCK FUCK")
    elif "false" in output:
        print ("Solid.")
    else:
        "Can't read file"

read_text("/Users/timisenman/Desktop/hey")
