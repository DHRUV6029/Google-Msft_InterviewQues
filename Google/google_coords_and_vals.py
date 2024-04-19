# I recently had a telephonic round with Google and faced the following question :

# Given a 1 Dimentional array having co-ordinates: x_1 < x_2 ....x_n , which has corresponding values : v_1 , v_2 ... v_n . Find the indexes of the co-ordinates that maximizes the equation : val_x + val_y + dist(x_y - x_x) ,where x_x and x_y are coordinates and val_x and val_y are their corresponding values respectively .

# My code :


coords  = [0,1]
vals  = [1,2]

if len(coords)<2:
    print(-1)
    
best_so_far = vals[0] + coords[0]
ans = 0
for j in range(1, len(vals)):
    j_vals = vals[j] - coords[j]
    
    ans = max(ans , best_so_far + j_vals)
    
    best_so_far = max(best_so_far , vals[j]+coords[j])
    
print(ans)
    