string = ["Hi, this is a butt"]

def add_to_index(index, keyword, url):
    for i in index:
        if i[0] == keyword:
            i[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

add_page_to_index(string, "whatwhat.com", "in the butt")

print string

