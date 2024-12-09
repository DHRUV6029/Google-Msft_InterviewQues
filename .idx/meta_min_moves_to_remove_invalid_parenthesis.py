class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        open, unclosed , deleteclosed = 0,0,0
        ans = ''
        for i in range(0,len(s)):
            if s[i] == '(':
                open+=1
                unclosed+=1

            elif s[i] == ')':
                if unclosed:
                    unclosed-=1

                else:
                    deleteclosed+=1

        opens = open - unclosed

        for i in range(0,len(s)):
            if s[i] == '(':
                if opens:
                    opens-=1
                    ans+=(s[i])
            elif s[i]==')':
                if deleteclosed:
                    deleteclosed-=1
                else:
                    ans+=s[i]
            else:
                ans+=s[i]

        return ans
