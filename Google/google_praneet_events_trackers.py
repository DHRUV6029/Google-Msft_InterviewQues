# 1 • /** A entry/exit event recorded at building entrance */
# 2- interface Event {
# 3
# String badgeId();
# 4
# boolean isEntry);
# // If false, event is Exit
# 5
# int timestamp(): // # of seconds since midnight
# 6
# 7
# 8
# 10
# / Print max number of people in the building and timestamp when it occurs
# 9- void findMaxOccupancy (Event[] events) ‹
# Implement me!
# 11
# uLG
class Event:
    def __init__(self ,id , isEnter , timeStamp) -> None:
        self.badgeId = id
        self.isEnter = isEnter
        self.timeStamp = timeStamp
        
        
def findMaxOccupancy(events):
    #assuming events are not sorted
    events = sorted(events, key=lambda x : (x.timeStamp , not x.isEnter))
    # here i am assuming the scaenario where Enter and Exit is at the same time prioritoze enter 
    #first
    
    max_occupancy = 0
    max_timestamp = 0
    
    cur_occupancy = 0
    for event in events:
        if event.isEnter:
            cur_occupancy+=1
        else:
            cur_occupancy-=1
            
            
        if max_occupancy < cur_occupancy:
            max_occupancy = cur_occupancy
        
            
        print("TimeStamp : "+ str(event.timeStamp) + "------> " + "MaxOccupancy " + str(max_occupancy) )
            
    
    
    
events = [
    Event(1, True, 160),  # Example timestamps
    Event(2, False, 111),
    Event(3, True, 111),
    # Add more events as needed
]

findMaxOccupancy(events)
    

