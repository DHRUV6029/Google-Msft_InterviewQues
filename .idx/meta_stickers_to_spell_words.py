sticker = "abc"
target = "aaaa"

sticker_mp = Counter(sticker)

target_mp =  Counter(target)

ans = 0

for k , v in target_mp.items():
    if k not in sticker_mp:
        print(-1)
        break

    if v > sticker_mp[k]:
        ans = max(ans , v//sticker_mp[k])

print(ans)
    
