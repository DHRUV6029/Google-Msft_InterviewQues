class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def get_sum(nums):
    
            mp = collections.defaultdict(list)

            for i in range(1 , len(nums)+1):
                tmp = []

                for comb in combinations(nums , i):
                    tmp.append(sum(comb))

                mp[i] = tmp

            return mp



        n = len(nums)//2
        left , right = get_sum(nums[:n]) ,get_sum(nums[n:])

        ans = abs(sum(nums[:n]) - sum(nums[n:]))


        #ideally target should be 0 means sum of each half should be == sum(nums)//2

        target = sum(nums)//2

        #MIM algorithm
        for k in range(1 , n+1):
            l = left[k]  #took k elemnerts from left 
            r = right[n-k] #took remainng n-k elemnts from right
            r.sort()   #no need of this step in java with treeset or builtin sorted set in python set in python is unordered
            #now for each sum in left find the remainng in the right part
            for lc in l:
                rc = target - lc
                idx = bisect.bisect_left(r , rc)

                for j in [idx, idx-1]:
                    if 0 <= j <= len(r)-1:
                        a = lc + r[j]
                        b = sum(nums) - a

                        ans = min(ans , abs(a-b))


        return(ans)
        

        
