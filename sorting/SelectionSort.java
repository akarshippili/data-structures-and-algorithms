public class SelectionSort implements SortingAlgorithm{
    @Override
    public int[] sort(int[] arr) {

        for(int i=arr.length-1; i>=1; i--){
            int max = Integer.MIN_VALUE;
            int index = -1;

            for(int j=0; j<=i; j++){
                if(arr[j]>max){
                    max = arr[j];
                    index = j;
                }
            }

            arr[index] = arr[i];
            arr[i] = max;

        }

        return arr;
    }
}

//time: theta(n^2) space: O(1)
