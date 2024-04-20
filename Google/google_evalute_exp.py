# https://leetcode.com/discuss/interview-question/351147/google-onsite-arithmetic-expression-to-construct-a-value
import collections
def arithemeticExpression(nums, target):
    cnt = collections.Counter(nums + list('+-*/()'))
    # build the directed graph
    G, S, S1 = collections.defaultdict(set), set(nums), set(x for x in nums if x >= 0)
    for x in S: G[x] = set('*-+/)')
    for op in '+-*/': G[op] = S1 | {'('}
    G['('], G[')'] = S, set('*-+/')
    
    ans = []
    def helper(expr, node):
        # already found an answer, just return
        #if len(ans) > 0: return True
        # the current node cannot be visited
        if cnt[node] == 0: return False
        # invalid brace, ) comes before (
        if node == ')' and cnt['('] == 1: return False
        # update expression
        expr, value = expr + str(node), None
        # check if the expression is valid
        valid = expr[-1] == ')' or (expr[-1].isdigit() and cnt['('] == 1)
        if valid:
            try:
                # replace float division to integer division
                value = eval(expr.replace('/', '//'))
                # print(expr, value)
            except:
                # handle divide zero case like 2 / (4 - 3 - 1)
                value = None
        if value == target:
            ans.append(expr)
            
            
        else:
            cnt[node] -= 1
            for nb in G[node]:
                # prune +-*/ zero, since it is redandant
                if node in set('+-*/') and nb == 0: continue
                # prune */ 1, since it is redandant
                if node in set('*/') and nb == 1: continue
                if helper(expr, nb): return True
            cnt[node] += 1
            return False
    
    for node in S | {'('}:
        helper('', node)
    return ans
    


nums = [1, 2, 3, 8, 4]  
target = 44
print(arithemeticExpression(nums, target))


