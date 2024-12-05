class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = []
        st = []

        for i in range(0,len(s)):
            if s[i] == "(":
                st.append((s[i], i))
            elif s[i] == ")":
                if st and st[-1][0] == "(":
                    st.pop()
                else:
                    st.append((s[i], i))
            
        res = ''

        for i in range(0 ,len(s)):
            if st and i == st[0][1]:
                st.pop(0)
                    #need to remove this
                continue
            else:
                res+=s[i]
        return res
