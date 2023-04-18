import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class NextGraterTemp {

    public static <T extends Comparable> List<Integer> getNextGraterTemp(List<T> tempartures){
        
        ArrayList<Integer> ans = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        
        for(int index = tempartures.size() -1; index>=0; index--){
            T temp = tempartures.get(index);
            
            while(!stack.empty() && tempartures.get(stack.peek()).compareTo(temp) != 1){
                stack.pop();
            }
            
            if(stack.isEmpty()) {
                ans.add(-1);
            } else {
                ans.add(stack.peek() - index);
            }
            
            stack.push(index);
        }

        Collections.reverse(ans);
        return ans;
    }

    public static void main(String[] args) {
        ArrayList<Double> input  = new ArrayList<>();
        // Arrays.asList()
        // input.add(73);
        // input.add(74);
        // input.add(75);
        // input.add(71);
        // input.add(69);
        // input.add(72);
        // input.add(76);
        // input.add(73);

        // 78.6,25.2,36.5,83.5,71.5
        input.add(78.6);
        input.add(25.2);
        input.add(36.5);
        input.add(83.5);
        input.add(71.5);


        List<Integer> ans = getNextGraterTemp(input);
        System.out.println(ans);
    }

}