#Given a log file of inputs with functions and timestamp:
import collections


logs = ["foo 0",
"bar 10",
"bar 30",
"foo 50"]


track  = set()
st = []
cur_time = 0

res = collections.defaultdict(int)

for i in range(0,len(logs)):
    log_name = logs[i].split(" ")[0]
    ts = int(logs[i].split(" ")[1])

    if log_name not in track:
        #this is the first time we are seeing the call
        if st:
            #pev function ends here
            res[st[-1][0]]+=(ts - cur_time)
        st.append((log_name , ts))
        track.add(log_name)
    else:
        res[st[-1][0]]+=(ts - cur_time)
        st.pop()
        track.remove(log_name)
    cur_time = ts

print(res)


