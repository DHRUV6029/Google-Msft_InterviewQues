class Solution {
private:
void generatePermutations(vector& nums, unordered_set& st, int& maxEle) {
if (nums.size() == 1) {
st.insert(nums[0]);
maxEle = max(maxEle, nums[0]);
return;
}

    for (int i = 0; i < nums.size() - 1; i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            int op1 = nums[i];
            int op2 = nums[j];
            nums.erase(nums.begin() + j);
            nums.erase(nums.begin() + i);

            int res = op1 * op2;
            nums.push_back(res);
            generatePermutations(nums, st, maxEle);
            nums.pop_back();

            res = op1 + op2;
            nums.push_back(res);
            generatePermutations(nums, st, maxEle);
            nums.pop_back();

            res = op1 - op2;
            nums.push_back(res);
            generatePermutations(nums, st, maxEle);
            nums.pop_back();

            res = op2 - op1;
            nums.push_back(res);
            generatePermutations(nums, st, maxEle);
            nums.pop_back();

            if (op2 != 0) {
                res = op1 / op2;
                nums.push_back(res);
                generatePermutations(nums, st, maxEle);
                nums.pop_back();
            }

            if (op1 != 0) {
                res = op2 / op1;
                nums.push_back(res);
                generatePermutations(nums, st, maxEle);
                nums.pop_back();
            }

            nums.insert(nums.begin() + i, op1);
            nums.insert(nums.begin() + j, op2);
        }
    }
}
public:
int findSmallestInteger(vector& nums) {
int maxEle = INT_MIN;
unordered_set st;
generatePermutations(nums, st, maxEle);

    for (int i = 1; i <= maxEle; i++) {
        if (st.find(i) == st.end()) {
            return i;
        }
    }
    return maxEle + 1;
}
};