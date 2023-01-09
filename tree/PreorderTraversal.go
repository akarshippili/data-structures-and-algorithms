/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func helper(cur *TreeNode, ans *[]int){
    if(cur == nil){
        return
    }

    *ans = append(*ans, cur.Val)
    helper(cur.Left, ans)
    helper(cur.Right, ans)
}

func preorderTraversal(root *TreeNode) []int {
    ans := []int{}
    helper(root, &ans)
    return ans
}
