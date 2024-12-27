import collections

#Q1
class Solution1:
    def generate_combinations(self,arr,n):
        ans = []

        mp = collections.defaultdict(int)

        for i in range(len(arr)):
            mp[arr[i]] = i

        def get_last_idx(ch):
            return mp[ch]
    
        
        def backtrack(i  , path):
            
            if len(path)==n:
                ans.append(path[:])
                return
            
            for j in range(i ,len(arr)):
                if not path or j - get_last_idx(path[-1]) -1 == 0: 
                    path.append(arr[j])
                    backtrack(j+1  , path )
                    path.pop()

        backtrack(0 , [])
        return ans

#Q2
class Solution:
    def generate_combinations_with_skip(self,arr,n ,k):
        ans = []
        mp = collections.defaultdict(int)

        for i in range(len(arr)):
            mp[arr[i]] = i

        def get_last_idx(ch):
            return mp[ch]
        
        def backtrack(i  , path , skips):
            #early pruning
            remain = n - len(path)
            if remain > len(arr)-i:
                return
            
            if len(path)==n:
                ans.append(path[:])
                return
            
            for j in range(i ,len(arr)):
                new_skip = 0
                if path:
                    new_skip = j - get_last_idx(path[-1]) - 1  #o(1) index lookup

                total_skips = skips+new_skip

                if total_skips <= k:
                    path.append(arr[j])
                    backtrack(j+1  , path , total_skips)
                    path.pop()

        backtrack(0 , [] ,0)
        return ans

            


arr = ['a', 'b', 'c', 'd', 'e','f','g']
n = 3
k = 2
s1 = Solution().generate_combinations_with_skip(arr , n ,k)
s2 = Solution1().generate_combinations(arr , n) 

print(len(s1))





