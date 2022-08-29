class Solution {
    public String removeStars(String s) {
        Stack<Character> stack = new Stack();
        
        for(char ch: s.toCharArray()){
            if(ch=='*' && stack.isEmpty()) return "";
            else if(ch=='*') stack.pop();
            else stack.push(ch);
        }
        
        StringBuffer sb = new StringBuffer();
        
        while(!stack.isEmpty()) sb.append(stack.pop());
        
        return sb.reverse().toString();
        
    }
}
