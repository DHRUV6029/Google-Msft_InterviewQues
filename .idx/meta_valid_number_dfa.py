class Solution:
    def isNumber(self, num: str) -> bool:
        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},         # state 0: start
            {"digit": 1, "dot": 4, "exponent": 5},     # state 1: digit
            {"digit": 1, "dot": 3},                    # state 2: sign
            {"digit": 4},                              # state 3: dot
            {"digit": 4, "exponent": 5},               # state 4: decimal
            {"sign": 6, "digit": 7},                   # state 5: exponent
            {"digit": 7},                              # state 6: exponent sign
            {"digit": 7}                               # state 7: exponent digit
        ]

        cur_state = 0
        group = ''
        valid_end = [1,4,7]
        for i in range(0,len(num)):
            cur = num[i]

            if cur.isdigit():
                group = 'digit'
            elif cur == '+' or cur == '-':
                group = 'sign'
            elif cur == '.':
                group = 'dot'
            elif cur == 'e' or cur == 'E':
                group = 'exponent'
            else:
                return False
            
            if not group  in dfa[cur_state]:
                return False
            
            cur_state = dfa[cur_state][group]


        return True if cur_state  in valid_end else False
