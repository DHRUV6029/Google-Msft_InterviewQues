# given a string with combination of operators & operands. The numbers are floating point integers. Process the string to find the final result.
# Operators will be fixed length corresponding to their usual meaning ie add, mul, sub, pow, div
# see examples below

# add(1,2)
# mul(2e3, sub(4,2))
# add(2.4, pow(2,4e4.5))
# overflows & division by 0 will not be there.

# Hint for c++ users use strtod()
print(2**43)
s = "add(2, pow(2,43))"

def pow(a , b):
    return a**b

def add(a ,b):
    return a+b

def div(a , b):
    return a/b

def mul(a , b):
    return a*b

def sub(a , b):
    return a-b


def apply(op1 , op2  , operand):
    if operand == 'pow':
        return pow(op1, op2)
    if operand == 'add':
        return add(op1 , op2)
    if operand == 'div':
        return div(op2, op1)
    if operand == 'sub':
        return sub(op2 , op1)
    



st1 = []
st2 = []
i = 0
while i <len(s):
    if s[i] == ',' or s[i] == " ":
        i+=1
        continue

    if s[i] == "(":
        st1.append(s[i])
    
    if s[i].isnumeric():
        num = ''
        while i < len(s) and s[i].isnumeric():
            num+=(s[i])
            i+=1
        i-=1
        
        st1.append(int(num))

    if s[i].isalpha():
        alp = ''
        while i < len(s) and s[i].isalpha():
            alp+=(s[i])
            i+=1
        i-=1

        st2.append(alp)


    if s[i] == ")":
        op1 , op2 = 0  ,  0
        operand= ""
        if st1 and st2:
            op1 = st1.pop()
            op2 = st1.pop()
            operand = st2.pop()
            st1.pop()

        ans = apply(op2, op1, operand)
        st1.append(ans)

    i+=1

print(ans)





