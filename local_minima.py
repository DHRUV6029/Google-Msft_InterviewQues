#find local maxima or minima in a aary

arr = [6,2,4,1,5]

def find_local_minima(arr , l , r):
    m = (l+r)//2

    #exit / base condition

    if (m == 0 or arr[m-1] > arr[m]) and (m == len(arr)-1 or arr[m] < arr[m+1]):
        return m #return the index

    if m > 0 and arr[m-1]  < arr[m]:
        return find_local_minima(arr , l  , m-1)

    return find_local_minima(arr , m+1  , r)


print(find_local_minima(arr , 0 , len(arr)-1))

    

