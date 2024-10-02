arr = [0,1,1,2,2,1,2,2,3,3,2,3]
amount =  {}
amount[0] = [0]

for i in range(1,len(arr)):
    if arr[i] == 1:
        amount[i] = [i]
        continue

    amount_to_make = i
    coins_to_make = arr[i]
    for j in range(1,i):
        remian_amount_to_make = i - j
        remian_coins_to_make = arr[i]-arr[j]

        if remian_amount_to_make in amount and len(amount[remian_amount_to_make])==remian_coins_to_make:
            v = [j for _ in range(arr[j])]
            v.extend(amount[remian_amount_to_make])
            amount[i] = v
            break

print("etst")
        
