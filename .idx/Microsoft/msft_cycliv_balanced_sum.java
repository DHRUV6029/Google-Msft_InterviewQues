import java.util.*;


public class Main {
    public static void main(String[] args) {
        int[] nums = new int[]{4,3,1,2,2,1};
        System.out.println(getCyclicBalancedSum(nums));

    }

    public static  int getCyclicBalancedSum(int[] nums){
        TreeMap<Integer  , Integer> treeMap = new TreeMap<>();

        for(int i = 0 ; i < nums.length ; i++){
            treeMap.put(nums[i] , treeMap.getOrDefault(nums[i] , 0)+1);
        }
        int prev = -1;
        int cur = 0;
        int maxCount = 0;

        for(var entry : treeMap.entrySet()){
            int key = entry.getKey();
            int count = entry.getValue();

            if(prev == -1 || Math.abs(prev - key)!=1){
                //break at this point
                cur = count;
                maxCount = Math.max(maxCount , cur);
            }else if(count == 1){
                cur+=count;
                maxCount = Math.max(maxCount, cur);
                cur = 1;

            }else{
                cur+=count;
                maxCount = Math.max(maxCount, cur);

            }


            prev = key;

        }

        return maxCount;


    }
}
