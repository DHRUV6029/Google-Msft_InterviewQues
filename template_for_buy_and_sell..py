import java.util.HashMap;
import java.util.TreeSet;

public class App{
    public static void main(String[] args) {
        
        
    }

    public static int solution(int [] prices , int k){
        int[][][] dp = new int[prices.length][k][2];

        for(int i = 0 ; i < prices.length ; i++){
            for(int j = 0 ; j < prices.length ; j++){
                dp[i][j][0] = Integer.MIN_VALUE;
                dp[i][j][1] = Integer.MIN_VALUE;
            }
        }

        //initial state
        dp[0][0][0] = 0;
        dp[0][1][1] = -prices[0]; // this indicates you have bought at index i so profit is -prices[i]

        for(int i = 1 ; i < prices.length ; i++){
            for(int j = 0  ; j<=k  ;j++){
                //at this index you are trying to do a transaction 
                dp[i][j][0] = Math.max(dp[i-1][j][0], prices[i] + dp[i-1][j][1]);
                //you can either do nothing if sold prev or sell here if holding on prev sta

                if(j > 0){
                    dp[i][j][1] = Math.max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i]);
                }

            }
        }
        int res = 0;
        for (int j = 0; j <= k; j++) {
            res = Math.max(res, dp[prices.length - 1][j][0]);
        }

        return res;
    }



    
}

