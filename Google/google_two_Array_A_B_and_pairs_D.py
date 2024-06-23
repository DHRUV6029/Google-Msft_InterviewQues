# Question: Given two arrays A and B, each of size n, where A[i], B[j] represent the strength of a signal received from 2 antennas placed at two different places. A signal is considered to be valid if it is present in both the arrays A & B at a distance <= D. Find the number of valid signals.

# Example: A=[1,3,4,3,4,5,6], B=[4,1,8,7,6,3,2], D=2
# Answer: The valid signals are A[0] (=B[1]), A[2] (=B[0]), A[3] (=B[5]). Hence the answer is 3.

# Solution: Solved using a sliding window of size 2d+1 storing the frequency of each signal value from B. Start traversing the array A and as we move forward to element A[i], add the element B[i+d] to the sliding window and remove element B[i-d] from the silding window. If the frequency for A[i]>0 in the current sliding window, increment the answer and decrease the frequency for A[i] in the window.

# Interviewer was happy with the solution.
import collections
A=[1,3,4,3,4,5,6]
B=[4,1,8,7,6,3,2]
D=2

window = collections.defaultdict(int)
ans = 0
for i in range(0, D+1):
    window[B[i]]+=1

if A[0] in window:
    ans = ans + window[A[0]]

l = 0
for i in range(1, len(A)):
    window[B[i+D]]+=1

    if sum(window.values()) > (2*D+1):
        window[B[l]]-=1
        if not window[B[l]]:
            window.pop(B[l])
        l+=1

    #check if A[i] is in the window
    if A[i] in window:
        ans = ans + window[A[i]]

print(ans)





