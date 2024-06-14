https://leetcode.com/discuss/interview-question/5314578/Microsoft-OA-Codility

import java.util.*;


public class Main {
    public static void main(String[] args) {
        int[] nums = new int[]{9,9,8,7,6};
        var res = solution(nums);
        for(int i = 0 ; i < res.length ; i++){
            System.out.println(res[i]);
        }

    }

    public static int[] solution(int[] nums){
        TreeSet<Integer> treeSet= new TreeSet<Integer>();
        int[] ans = new int[nums.length];
        int maxVals = Integer.MIN_VALUE;
        for(int i=0; i<nums.length; i++){
            maxVals  = Math.max(maxVals, nums[i]);
        }
        int[] freq = new int[maxVals+1];
        for(int i = 0 ; i < nums.length ; i++){
            freq[nums[i]]+=1;
        }
        for(int i = freq.length-1 ; i >= 0 ; i--){
            if(freq[i]>1){
                int dups = freq[i]-1;
                freq[i] = 1;
                freq[i-1]= freq[i-1]+dups;

            }
            if(freq[i]==1) {
                treeSet.add(i);
            }
        }
        for(int i = 0 ; i < nums.length ; i++){
            int val = treeSet.floor(nums[i]);
            ans[i] = val;
            treeSet.remove(val);
        }
        return ans;
    }
}
