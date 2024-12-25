class Solution:
    def myAtoi(self, s: str) -> int:
        digit = "0123456789"

        dfa = {
            "+" : [digit],
            "-" : [digit],
            digit : [digit],
            " " : [" " , "+" , "-" , digit],
            'start'  : [" " , "+" , "-" , digit]
        }

        cur_state = "start"
        digits = 0
        sign = 1

        def get_digit(digit, sign):
            digit = digit * sign
            if digit > 2**31 - 1:
                return 2**31 - 1
            if digit < -2**31:
                return -2**31
            return digit

        for i in range(0,len(s)):
            ch = s[i]
            #representanion of the current state of digit
            if ch.isdigit():
                ch = digit

            if ch in dfa[cur_state]:
                cur_state = ch
            else:
                return get_digit(digits, sign)
            
            if cur_state == "+" or cur_state == "-":
                sign = 1 if cur_state == "+" else -1

            if cur_state in digit:
                digits = digits * 10 + int(s[i])

        return get_digit(digits, sign)
