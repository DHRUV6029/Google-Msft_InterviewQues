# You are given a string s containing only the characters '(', ')', '{', '}', '[' and ']'. Your task is to determine if the input string is valid according to the following rules:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Additionally, this problem introduces a new rule:
# 3. Each open bracket must be paired with a corresponding closing bracket in a unique way. That is, for each open bracket, there should not be multiple options for the corresponding closing bracket.

# Write a function isValidUnique(s) that returns true if s is valid and false otherwise.

s=  "{[(])}"

st = []



for i in range(0,len(s)):
    
    if s[i] == '(' or s[i] == '{'  or s[i] == '[':
        st.append(s[i])
        
    elif st and ((st[-1] == '(' and  s[i] == ')')  or ((st[-1] == '[' and  s[i] == ']')) or ((st[-1] == '{' and  s[i] == '}'))):
        st.pop()
    else:
        print(False)
        
        break
    
print(True)
    