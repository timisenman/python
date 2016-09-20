from Person import Person

timInfo = {
    'id': 1,
    'username': 'brokensword',
    'password':'ilovexavi'
}

tim = Person(timInfo)
print tim.username

def authenticateUser(username, password):
    if username == tim.username and password == tim.password:
        print 'Logged in!'
    else:
        print 'Fuck you'
        
authenticateUser('brokensword', 'iloveelaine') 	