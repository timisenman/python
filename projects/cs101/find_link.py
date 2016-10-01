link = "https://fuck.me/"

start_link = find.link('"')
end_link = find.link('"', start_link+1)
web_link = [start_link+1:end_link]

print web_link


    
