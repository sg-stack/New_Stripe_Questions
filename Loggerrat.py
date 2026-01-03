"THIS IS A LEETCODE PROBLEM LOGGER RATE DO NOT FORGET"
"Good thing to edit this message out very quickly"
"This is easy level leetcode problem"
class LoggerRateLimit:
    def __init__(self):
        self.limiter={}
    def shouldPrintMessage(self,timestamp,message):
        if message not in self.limiter:
            self.limiter[message]=timestamp
            return True
        else:
            if timestamp-self.limiter[message]>=10:
                self.limiter[message]=timestamp
                return True
            else:
                return False
m=LoggerRateLimit()
print(m.shouldPrintMessage(1, "foo"))
print(m.shouldPrintMessage(2, "bar"))
print(m.shouldPrintMessage(3, "foo"))
print(m.shouldPrintMessage(8, "bar"))
print(m.shouldPrintMessage(11, "foo"))
print(m.shouldPrintMessage(12, "bar"))


