public class BubbleSort implements SortingAlgorithm{

    @Override
    public int[] sort(int[] arr) {
        for(int i=0; i < arr.length-1; i++){
            for(int j=0; j < arr.length-i-1; j++){
                if(arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
        return arr;
    }

}

// time: theta(n^2)
// space : theta(1)



// can use swap flag to check if ( arr is sorted before all the comparison ) to break out of the loop;

// in one iteration if no swaps
// arr is sorted
// break out of loop
