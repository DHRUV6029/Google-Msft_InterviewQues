# Validate if the equation is syntactically correct.

# Valid operators: +, -, a-z, (, )
# Test cases:
# Valid - a + x = b + (c + a)
# Invalid - a + x = (ending with =; doesn't have RHS)
# Invalid - a + -x = a + b (- in -x is a unary operator)


eqaution = "( a - b ) = b"  #keeping space seprated for ease of parsing 


alpha = 'abcdefghijklmnopqrstuvwxyz'
dfa_map = {
    '#' : ['(', alpha , '-' , '+'],
    '(' : [alpha , '-' , '+' ,'('],  #not sure if +1+2 is valid or not if not remoce + from state machine
    ')' : ['+' , '-' , ')'],
    alpha : ['+' , '-' , ')'],
    '+' : ['(' , alpha],
    '-' : ['(' , alpha],  
}

#extra check
end_states = [")", alpha]

#will do some precheck before parsing the the eqaution
#will take in as a list for traversal simplicity
eqaution = eqaution.split("=")


    
lhs = eqaution[0].split(' ')[:-1]
rhs = eqaution[1].split(' ')[1:]

if not lhs or not rhs:
    print('Invalid')

def parse_equations(vals):
    balance = 0
    
    cur_state = "#" #start from somewhere
    i = 0
    while i < len(vals):
       
        next_valid_states = dfa_map[cur_state]
        
        actual_next_state = vals[i]
        if actual_next_state == '(':balance+=1
        if actual_next_state == ')': balance-=1
        
      
        #check if we can go ahead or not
        if not any(actual_next_state in state for state in next_valid_states):
            return False
        
        if i == len(vals)-1 and actual_next_state in end_states:
            return (True and balance == 0)
        
        cur_state = actual_next_state
        #################################
        if cur_state in alpha:
            cur_state = alpha
        #################################
        i+=1
        
   
    return True if balance == 0 else False


if parse_equations(lhs):
    if parse_equations(rhs):
        print('Valid')
    else:
        print('Invalid')
else:
    print('Invalid')
    
    
    
