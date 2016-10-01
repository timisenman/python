class Person(object):

    def __init__(self, info):
        self.password = info['password']
        self.id = info['id']
        self.username = info['username']

    def setInfo(self, data):
        self.password = data.password
        self.id = data.id
        self.username = data.username

    def sendMessage(self, message):
     	print 'message setnt ' + message
