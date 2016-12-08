import bot

wally = bot.Robot("A pretty head", "Raspberri Pi")

print wally.body
print "and " + wally.head

print "+++++++++"

wally = bot.Head("Intel i7", "Canon 5D", "Sony", "Sennheiser")

wally.talkHead()