class Solution {
    public int trap(int[] height) {
     
        int ans = 0;
        int index = 0;
        
        Stack<StackNode> stack = new Stack<>();
        
        while(index<height.length){
            
            int popedHeight = 0;
            
            while(!stack.empty() && height[index]>stack.peek().height) {
                ans += (stack.peek().height - popedHeight) * (index - stack.peek().index - 1);
                popedHeight = stack.peek().height;
                stack.pop();
            }
            
            if(!stack.empty()) ans += (height[index] - popedHeight) * (index - stack.peek().index - 1);
            stack.push(new StackNode(height[index], index));
            index++;
        }
        
        
        return ans;
    }
}


class StackNode{
    int height;
    int index;
    
    public StackNode(int height, int index){
        this.height = height;
        this.index = index;
    }
    
    public String toString(){
        return this.height + " " + this.index;
    }
    
}
