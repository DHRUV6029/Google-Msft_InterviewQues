# Round 3:
# Question: You are receiving signals from a robot at different timestamps (in non-decreasing order). There could be duplicate messages. Print only the messages that are unique in the last 10 seconds.
# Follow-up: Classify duplicate messages as bugs. Don’t print a message if it’s repeated within the 10 seconds window (future or Past).
# Input:
# [{timeStamp: 1, message: "Hello"}, {timeStamp: 2, message: "Hello"}, {timeStamp: 8, message: "Hey"}, {timeStamp: 12, message: "Hello"}]
# Output: Hello Hey Hello
# Follow-up Output: Hey Hello (First "Hello" is excluded due to duplicates within a 10-second window).
# Solution: Solved both the main problem and follow-up. I thought it went well, but the feedback was that my approach wasn’t optimized, and they were looking for more scalable solutions.
# Feedback: Lean not hire.

import collections
mp = {}

logs = [
  {
    "timeStamp": 1,
    "message": "Hello"
  },
  {
    "timeStamp": 2,
    "message": "Hello"
  },
  {
    "timeStamp": 8,
    "message": "Hey"
  },
  {
    "timeStamp": 12,
    "message": "Hello"
  }
]



# def print_log(message):
#     print(message)


# def check_validitity_for_print(message , timestamp):
#     if message not in mp:
#         print(message)
#     else:
#         last_stream_time = mp[message]

#         if timestamp - last_stream_time >=10:
#             print_log(message)

#     mp[message] = timestamp


# for log in logs:
#     check_validitity_for_print(log["message"], log["timeStamp"])



mp = collections.defaultdict(list)
def print_log(message_stream):
    for k, v in mp.items():
        for m in v:
            print(m)





def check_validity_for_print(mesaage, timestamp):
    if mesaage not in mp:
        mp[mesaage].append((mesaage , timestamp))

    else:
        st = mp[mesaage]
        is_flagged =  False
        while st and st[-1][1] - timestamp < 10:
            is_flagged = True
            st.pop()

        if not is_flagged:
            st.append((mesaage , timestamp))

for log in logs:
    check_validity_for_print(log["message"], log["timeStamp"])

print(print_log(mp))
        
