import java.util.TreeSet;

public class App{
    public static void main(String[] args) {
        int[][] operations = new int[][] {{1,39},{2 ,-154, 143},{2,55,55},{1,-43},{2,57,29},{2,55,26},{2,-48,151}};
        String ans = solution(operations);
        System.out.println(ans);
        
    }

    static String solution(int[][] operations){
        StringBuilder ans = new StringBuilder();
        TreeSet<Integer> treeSet = new TreeSet<>();

        for(int[] command : operations){
            if(command[0]==1){
                treeSet.add(command[1]);
            }else{
                int s = 0;      
                int e = 0;
                if(command[1] < 0){    
                    e = command[1]+1;        
                    s = command[1] - command[2];   
                }else{
                    e = command[1]-1;
                    s = command[1] - command[2];
                }
                var left = treeSet.ceiling(s);     
                var right = treeSet.floor(e);
                
                if(left == null && right == null){
                    ans.append("1");
                }
                else if(left == null && right != null && s > right){
                    ans.append("1");      
                }
                else if(left != null && right == null &&  e < left){
                      ans.append("1");   
                }
                else if (left != null && right != null && e < left  && s > right){
                    ans.append("1");    
                }
                else{
                    ans.append("0");
                }
            }
        }
        return  ans.toString();
        

    }
}

