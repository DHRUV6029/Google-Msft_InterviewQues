# Given a set of photos ids (inclusive of favourite Ids), and favourite ids () (No duplicates in photos and favourites)
# Write a **iterator** that returns favourite photos ids then photos ids (in the given order),
# without any duplicate.
# Input:
# Photos: [p10,p2,p3,p4,p5,p6,p7,p8,....]
# Favourite: [p8,p4,p10]
# Output: 
# [p8,p4,p10,p2,p3,p5,p6,p7,....]
# Second Part: If Favourite is given in sorted order, how would you optimize, as I have used the hashset?

class PhotoIterator:
    def __init__(self , photos , favs) -> None:
        self.photos = photos
        self.favs = favs
        self.i = -1
        self.j = 0
        self.seen = set()

    def getNext(self):
        if self.i < len(self.favs)-1:
            #mark as done in photos array 
            self.seen.add(self.favs[self.i])
            self.i+=1
            return self.favs[self.i]
        
        else:
            while self.j < len(self.photos) and self.photos[self.j]  in self.seen:
                self.j+=1
            
            val = self.photos[self.j] if self.j < len(self.photos) else None
            self.j+=1

            return val
        


ans = []
obj = PhotoIterator(["p10" , "p2","p3","p4","p5","p6","p7","p8"], ["p8","p4","p10"])
ans.append(obj.getNext())
ans.append(obj.getNext())
ans.append(obj.getNext())
ans.append(obj.getNext())
ans.append(obj.getNext())
ans.append(obj.getNext())
ans.append(obj.getNext())
ans.append(obj.getNext())
ans.append(obj.getNext())
ans.append(obj.getNext())
            
print(ans)
        

