class Time:
    pass
    def printTime(time):
        print str(time.hours)+ ":" + str(time.minutes) + ":" + str(time.seconds)

    def increment(self,seconds):
        self.seconds = seconds + self.seconds
        while self.seconds >= 60:
            self.seconds = self.seconds - 60
            self.minutes = self.minutes + 1
        while self.minutes >= 60:
            self.minutes = self.minutes - 60
            self.hours = self.hours + 1

#Example calling two different objects of Time().
    # def after(self, time2):
    #     if self.hours > time2.hours:
    #         return 1
    #     if self.hours < time2.hours:
    #         return 0
    #     if self.minutes > time2.minutes:
    #         return 1
    #     if self.minutes < time2.minutes:
    #         return 0
    #     if self.seconds > time2.seconds:
    #         return 1
    #     return 0
    #     if doneTime.after(currentTime):
    #         print "The bread is not yet done."




currentTime = Time()
currentTime.hours = 9
currentTime.minutes = 14
currentTime.seconds = 30
currentTime.printTime()
currentTime.increment(500)
currentTime.printTime()

### Initialization Method ###
class Time():
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

currentTime = Time(9, 14, 30)
currentTime.printTime()
# >>>9:14:30

currentTime = Time()
currentTime.printTime()
# >>>0:0:0

currentTime = Time(9)
currentTime.printTime()
# >>>9:0:0

currentTime = Time(hours = 9, seconds = 30)
currentTime.printTime()
# >>>9:0:30

