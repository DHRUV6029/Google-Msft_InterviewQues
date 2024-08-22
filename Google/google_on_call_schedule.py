on_call = [['Abby', 1, 10] , ['Ben' ,5 ,7] , ['Carla' , 6, 12] , ['David' ,15 ,17]]

mp = collections.defaultdict(list)

for name , start , end in on_call:
    mp[start].append(name)
    mp[end].append(name)


ans = []
mp = dict(sorted(mp.items() , key=lambda x : x[0]))

cur_set = set()
last_used = -1
for k , v in mp.items():
   
    for name in v:
        if name in cur_set:
        
            tmp = copy.deepcopy(cur_set)
            ans.append((last_used , k , tmp))
            cur_set.remove(name)
        else:
            if cur_set:
                tmp = copy.deepcopy(cur_set)
                ans.append((last_used , k , tmp))
            cur_set.add(name)
        last_used =k
           
print(ans)
