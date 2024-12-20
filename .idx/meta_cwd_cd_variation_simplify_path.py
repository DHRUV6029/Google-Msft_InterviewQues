

cwd = '/a/b'
cd = './/c/../../d/f'

#edge case 
if cd[0] == '/':
    st  = []
else:
    st = cwd.split('/')

cd = cd.split('/')
    


def canonical_path(st , cd):
    #code will be same as simplfy path 

    for i in range(0,len(cd)):
        if cd[i] == '..':
            if st:
                st.pop()
        elif cd[i] not  in ['.' ,'']:
            st.append(cd[i])
    return st

ans  = canonical_path(st[1:] , cd)
print("/"+'/'.join(ans))

