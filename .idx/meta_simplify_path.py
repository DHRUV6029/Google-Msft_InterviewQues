class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/") #removes all the "/"
        st = []
        for name in path:
            if name == '..':
                if st: #only go back if you are not at the root
                    st.pop()
            elif name != '.' and name != '':
                st.append(name)

        return ("/"+'/'.join(st))
