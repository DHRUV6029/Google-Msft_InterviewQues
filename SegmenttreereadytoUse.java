class SegmentTree {
    int[] tree;
    int LEFT, RIGHT;

    public SegmentTree(int[] nums) {
        tree = new int[4*nums.length];
        LEFT = 0;
        RIGHT = nums.length-1;

        buildTree(nums, 0, LEFT, RIGHT);
    }

    private void buildTree(int[] nums, int index, int sLeft, int sRight) {
        if (sLeft == sRight) {
            tree[index] = nums[sLeft];
            return;
        }

        int mid = sLeft + (sRight-sLeft)/2;
        buildTree(nums, 2*index+1, sLeft, mid);
        buildTree(nums, 2*index+2, mid+1, sRight);

        tree[index] = tree[2*index+1] + tree[2*index+2];
    }

    public int sumQuery(int qLeft, int qRight) {
        return sumQuery(0, LEFT, RIGHT, qLeft, qRight);
    }

    private int sumQuery(int index, int sLeft, int sRight, int qLeft, int qRight) {
        // segment is completely outside the query range
        if (sLeft > qRight || sRight < qLeft)
            return 0;
        // segment is completely inside the query range
        if (sLeft >= qLeft && sRight <= qRight)
            return tree[index];
        
        int mid = sLeft + (sRight-sLeft)/2;

        int left = sumQuery(2*index+1, sLeft, mid, qLeft, qRight);
        int right = sumQuery(2*index+2, mid+1, sRight, qLeft, qRight);

        return left+right;
    }

    public void update(int index, int val) {
        update(0, LEFT, RIGHT, index, val);
    }

    private void update(int index, int sLeft, int sRight, int node, int val) {
        if (sLeft == sRight) {
            tree[index] = val;
            return;
        } else {
            int mid = sLeft + (sRight-sLeft)/2;

            if (node <= mid && node >= sLeft)
                update(2*index+1, sLeft, mid, node, val);
            else
                update(2*index+2, mid+1, sRight, node, val);
            
            tree[index] = tree[2*index+1] + tree[2*index+2];
        }
    }
}

class NumMatrix {

    SegmentTree[] trees;

    public NumMatrix(int[][] matrix) {
        trees = new SegmentTree[matrix.length];

        for (int i=0; i<matrix.length; i++) {
            trees[i] = new SegmentTree(matrix[i]);
        }
    }
    
    public void update(int row, int col, int val) {
        SegmentTree st = trees[row];
        st.update(col, val);
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int total = 0;

        for (int i=row1; i<=row2; i++) {
            total += trees[i].sumQuery(col1, col2);
        }

        return total;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * obj.update(row,col,val);
 * int param_2 = obj.sumRegion(row1,col1,row2,col2);
 */
