class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        
        int[][] ans = new int[matrix.length][matrix[0].length];
        
        for(int i = 0; i < matrix.length; i++){
            for( int j = 0; j < matrix[0].length; j++){
                ans[i][j] = -1;
            }
        }
        
        for(int i = 0; i < matrix.length; i++){
            for( int j = 0; j < matrix[0].length; j++){
                dfs(matrix, ans, i, j);
            }
        }
        
        
        // for(int[] x: ans) System.out.println(Arrays.toString(x));
        
        int max = 0;
        
        for(int i = 0; i < matrix.length; i++){
            for( int j = 0; j < matrix[0].length; j++){
                max = Math.max(max, ans[i][j]);
            }
        }
        
        return max+1;
    }
    
    // 
    
    
    public int dfs(int[][] matrix, int[][] ans, int sr, int sc){
        // System.out.println("start " + sr + " " + sc);
        
        if(ans[sr][sc]!=-1) return ans[sr][sc];
        
        int[][] dir = new int[][] {
            {-1,0},{0,1},{1,0},{0,-1}
        };
        
        
        for(int[] x: dir){
            int r = sr + x[0];
            int c = sc + x[1];
            if(r<0 || c<0 || r>=matrix.length || c>=matrix[0].length || matrix[r][c] <= matrix[sr][sc]) continue;
            ans[sr][sc] = Math.max(ans[sr][sc], dfs(matrix, ans, r, c));
        }
        
        // System.out.println(sr + " " + sc + " " + left + " " + right +" " + down + " " + left);
        ans[sr][sc] += 1;
        
        // System.out.println("end " + sr + " " + sc);
        return ans[sr][sc];
    }
    
    
    
    
}
