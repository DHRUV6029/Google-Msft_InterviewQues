s = "add(5, sub(pow(7 , 2), mul(3,2)))"

#types of opertions add , sub , pow , multiply , mod , divide


def operation(val , op1 ,op2):
    if val == "add":
        return op1 + op2
    elif val == "sub":
        return op2 - op1
    elif val == "mod":
        return op2 % op1
    elif val == "div":
        return op2 // op1  #assuming integer division
    elif val == "mul":
        return op1 * op2
    elif val == 'pow':
        return op2 ** op1
    

op_st = []
val_st = []
i = 0
while i < len(s):
    if s[i] == " " or s[i] == ",":
        i+=1
        continue

    if s[i] == "(":
        val_st.append("(")

    #if it is a digit
    digit = 0
    is_digit = False
    while i < len(s) and s[i].isnumeric():
        is_digit = True
        digit = digit * 10 + int(s[i])
        i+=1
    if is_digit:
        val_st.append(digit)
        i-=1

    #if it is a operator
    op = ''
    is_ops = False
    while i < len(s) and s[i].isalpha():
        op+=s[i]
        i+=1
        is_ops = True
    if is_ops:
        op_st.append(op)
        i-=1

    #if a closing bracket
    if s[i] == ')':
        op1 , op2 , operator = 0 ,0 , ""
        if len(val_st)>=3:
            op1 = val_st.pop()
            op2 = val_st.pop()

            val_st.pop() #opening  brackert 


        if op_st:
            operator = op_st.pop()

            val = operation(operator , op1, op2)

            val_st.append(val)

    i+=1

print(val_st[-1])





        
