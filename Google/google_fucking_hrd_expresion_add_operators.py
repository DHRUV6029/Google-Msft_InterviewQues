def generate_expressions(nums, operators, target):
    def backtrack(expr, idx, total, running_expr):
        if idx == len(nums):
            if total == target:
                valid_expressions.append(running_expr)
            return
        
        for op in operators:
            if idx > 0 and op == '/' and nums[idx] == 0:
                continue  # Skip division by zero
            if idx > 0 and op == '-' and nums[idx] == 0:
                continue  # Skip negative zero
            if op == '(':
                backtrack(expr, idx + 1, total, running_expr + '(')
            elif op == ')':
                backtrack(expr, idx + 1, total, running_expr + ')')
            else:
                if expr and expr[-1] not in operators:
                    backtrack(expr + op + str(nums[idx]), idx + 1, evaluate(total, nums[idx], op), running_expr + op + str(nums[idx]))
                else:
                    backtrack(expr + str(nums[idx]), idx + 1, nums[idx], running_expr + str(nums[idx]))
                    backtrack(expr + op + str(nums[idx]), idx + 1, evaluate(total, nums[idx], op), running_expr + op + str(nums[idx]))

    def evaluate(x, y, op):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y

    valid_expressions = []
    backtrack('', 0, 0, '')
    return valid_expressions

# Example usage
nums = [2, 3, 4]
operators = ['+', '-', '*', '/', '(', ')']
target = 20
expressions = generate_expressions(nums, operators, target)
for expr in expressions:
    print(expr)
