# In my interview I got the following question:
# Create a Phone Number System with the following functions:
# isAvailable(n) // returns if a number is available
# reserve(n) // reserve and assign a number
# getAvailableNumber() // return and assign a number.

# This seems very easy and I coded the solution using hashmap and interviewer said he is fine and ended the interview.
# I got negative feedback of this round. Was there anything I was missing. I coded and included all the edge cases. Can someone tell me if I missed anything in understanding?

# google
# interview

import heapq
class PhoneNumberSystem:
    def __init__(self , phone_numbers) -> None:
        self.avaliable = []
        self.reserved = set()
        for n in phone_numbers:
            heapq.heappush(self.avaliable , n)

    def is_avaliable(self , number):
        if number not in self.reserved:
            return number
        
        return "Number is not Avaliable"

    def __reserve__(self , number):
        if number not in self.reserved:
            self.reserved.add(number)
            return True
        
        return False

    def get_avaliable_number(self):
        while self.avaliable:
            candidate = heapq.heappop(self.avaliable)

            if candidate not in self.reserved:
                self.reserved.add(candidate)
                return candidate
            
        return "No numbers are avaliable!!!!"
    
obj = PhoneNumberSystem([1,2,3,5,6,4,8])
print(obj.is_avaliable(8))
obj.get_avaliable_number()
obj.get_avaliable_number()
obj.get_avaliable_number()
obj.get_avaliable_number()
print(obj.is_avaliable(1))

print("vmlrr")
