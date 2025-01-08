words = ["This", "is", "an", "example", "of", "text", "justi"]
maxWidth = 7


text = []

i = 0
cur_line = ''
while i < len(words):
    
    if len(cur_line)+ len(words[i]) <= maxWidth:
        cur_line+=words[i] + " "
    else:
        cur_line = cur_line.rstrip(' ')
        text.append(cur_line)
        cur_line = words[i] + " "


    i+=1

if cur_line:
    cur_line = cur_line.rstrip(" ")
    text.append(cur_line)

print(text)
