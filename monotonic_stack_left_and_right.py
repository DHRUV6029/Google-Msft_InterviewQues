def minimumLengthOfRanges(nums):
    st = [-1]
    
    left = [0]*len(nums)
    right = [0]*len(nums)
    
    for i in range(0,len(nums)):
        
        while st[-1] != -1 and nums[st[-1]] >= nums[i]:
            st.pop()
    
        left[i] = i - st[-1]

        st.append(i)

    st = [len(nums)]
    for i in range(len(nums)-1 ,-1 ,-1):
    
        while st[-1] != len(nums) and nums[st[-1]] >= nums[i]:
            r = st.pop()
    
 
        right[i]+=st[-1] - i -1
    
        st.append(i)

    return [left , right , pref]


#for max change the sign
