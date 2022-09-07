/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public String tree2str(TreeNode root) {
        String ans = helper(root);
        return ans.substring(1, ans.length()-1);
    }
    
    public String helper(TreeNode node){
        if(node==null) return "()";
        
        String ans = "";
        ans = ans + node.val;
        
        String left = helper(node.left);
        String right = helper(node.right);
        
        if(left.length()>=2 && right.length()>2) {
            ans = ans + left; 
            ans = ans + right;
        } else if(left.length()>2) ans = ans + left;
        
        return "(" + ans + ")";
    };
}
