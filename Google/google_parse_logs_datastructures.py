# I had a virtual phone screen interview with Google on 24th October 2023 - 3pm to 3:45pm MST. I think its safe to detail out the truth in its entirety considering I'm going to be posting this anonymously. So here goes -

# My Background:
# I should mention that I'm closing on 8 years of work experience. Although I haven't been fortunate enough to find a dev role right at the start of my career, I am in one now. I started out as a Content Writer at a Digital Marketing firm (earning $120/month) for a year, followed by 2.5 years in Functional Testing and Prod Support, then a Masters' with an internship where I did my first UI (real dev) project, then followed by another 2 years with a pseudo dev contract work, and finally a Full Stack for the past year.

# I was fortunate enough to even land this opportunity with Google, and I'm content that I didn't embarass myself as much. Anyway, pardon my sad background of a story, I just wanted to vent a little. I know I have ways to go, and I will keep at it.

# Anyway, here's my interview experience -

# Interviewer - Intro
# Me - Intro + Pleasantries
# Interviewer - Smiles > In the interest of time, he politely asks if I'm ready to get into the coding challenge.
# Me - (Nervous like a mother) Sure

# Question

# There's this text log file (single file) that contains a chat transcript of a chat room (can have multiple people talking).
# Something like the following -

# 10:00 <alice> Hi! What's up?
# 10:01 <bob> Hey
# 10:03 <alice> Dinner?
# 10:04 <john> I'm down! But only if it isn't vegan.
# .
# .
# .... could be more entries

import collections
import heapq
logs = ["10:00 <alice> Hi! What's up?", 
        "10:01 <bob> Hey",
        "10:04 <john> I'm down! But only if it isn't vegan", 
        "10:03 <alice> Dinner?"]

name_to_wpt = collections.defaultdict(int)
name_to_freq = collections.defaultdict(int)

max_heap = []
stale = set()

n = 2 # for tets


def parse_transaction(log):
    log = log.split(" ")
    word_cnt = len(log[2:])
    
    return [log[0] , log[1][1:len(log[1])-1] , word_cnt]

def get_result():
    #Eexpected result format [(name , wpt)] len will n
    
    res = []
    i = 0
    while i < min(n , len(max_heap)):
        if max_heap[i] not in stale:
            res.append((max_heap[i][1],name_to_wpt[max_heap[i][1]]))
            i+=1
        else:
            heapq.heappop(max_heap)
            
        
            
    return res if len(res)==n else  None
            
            

for transactions in logs:
    
    time_stamp , name , word_cnt = parse_transaction(transactions)
    #will retunrn the result after each operarions i,e after parsing each log
    
    
    ##########################################################################
    name_to_wpt[name] = (name_to_wpt[name] + word_cnt)/(name_to_freq[name]+1)
    name_to_freq[name]+=1
    
    entry = (-name_to_freq[name],name)
    #in_validate previous max_heap entry
    if name_to_freq[name]>1:
        stale.add((-(name_to_freq[name]-1) , name))
        
    heapq.heappush(max_heap , entry)
    ##########################################################################
    
    
    
    ans = get_result()
    
    print(ans)
    
    

