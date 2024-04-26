# Name	Start	End
# Abby	10	100
# Ben	50	70
# Carla	60	120
# David	150	300
import collections
table = [['Abby' ,10	,100],['Ben',50	,70] ,['Carla',	60	,120],['David'	, 150,	300]]

new_table = []
start = collections.defaultdict(list)
end = collections.defaultdict(list)

end_points = collections.defaultdict(int)

for name , s , e in table:
    start[s].append(name)
    end[e].append(name)
    
    end_points[s]+=1
    end_points[e]-=1
    
prev =0  
end_points = dict(sorted(end_points.items()))
is_first = None
for k , v in end_points.items():
    cur = []
    
    
        #get start name here
    name = start[k]
        
        
    new_table.append((k , name))
    is_first = 1
        
    
    
    
    
