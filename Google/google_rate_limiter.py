# Questions were in parts

# Implement given interface having one method
# Write a class/method to execute above method only once/second
# after implementing above 2, we had 15 min so he asked, for given n, we should allow n requests/sec.
# Overall it was variation of Rate Limiter.

# Result : Moving to onsite.
import collections
class Logger:

    def __init__(self):
        self.mp = collections.defaultdict(int)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.mp:
            self.mp[message] = timestamp+10
            return True
        
        else:
            if self.mp[message] <= timestamp:
                self.mp[message] = timestamp+10
                return True

        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)