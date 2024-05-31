class SegmentTree{         
        private int[] tree;
        private int n;
        //init tree
        public SegmentTree(int n){
            this.n=n;
            tree=new int[4*n+1];
        }
        
        public int query(int left,int right){
            return query(0,0,n-1,left,right);
        }
        
        private int query(int idx,int l,int r,int left,int right){
            if(r<left||right<l){
                return 0;
            }
            
            if(left<=l && r<=right){
                return tree[idx];
            }
            int m=l+(r-l)/2;
            int lMax=query(2*idx+1,l,m,left,right);
            int rMax=query(2*idx+2,m+1,r,left,right);
            return Math.max(lMax,rMax);
                      
        }
        
        public void update(int idx,int val){
            update(0,0,n-1,idx,val);
        }
        
        private void update(int idx,int l,int r,int updateIdx,int val){
            if(l==r){
                tree[idx]=Math.max(tree[idx],val);    
                return;
            }
            
            int m=l+(r-l)/2;
            if(l<=updateIdx && updateIdx<=m){
                update(2*idx+1,l,m,updateIdx,val);
            }else {
                update(2*idx+2,m+1,r,updateIdx,val);
            }
            tree[idx]=Math.max(tree[2*idx+1],tree[2*idx+2]);
        }
    
        public int max(){
            return tree[0];
        }
}
    

class Solution {     
    public int lengthOfLIS(int[] nums, int k) {
        SegmentTree segmentTree=new SegmentTree((int)(1e5)+1);
        for(int a:nums){
            int left= Math.max(0,a-k);
            int right= a-1;
            int currMax = segmentTree.query(left,right);
            segmentTree.update(a,currMax+1);
        }        
        return segmentTree.max();
    }
}
