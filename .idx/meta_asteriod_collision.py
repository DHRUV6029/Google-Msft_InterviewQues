class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        i = 0

        while i< len(asteroids):
            val = asteroids[i]
            while st and st[-1] > 0 and val<0:

                if abs(val) < abs(st[-1]):
                    val = 0
                    break
                elif abs(val) == abs(st[-1]):
                   #need to flip and process the stack again
                    top_stack =st.pop()
                    asteroids[i-1] = -top_stack
                    new_asteriod = -val
                    asteroids[i] = new_asteriod

                    i-=1
                else:
                    st.pop()
                

            if val != 0:
                st.append(asteroids[i])

            i+=1

        return st
                    
