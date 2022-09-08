public class QuickSort implements SortingAlgorithm{

    @Override
    public int[] sort(int[] arr) {
        System.out.println("using quick sort");
        quicksort(arr,0, arr.length-1);
        return arr;
    }

    public void public class QuickSort implements SortingAlgorithm{

    @Override
    public int[] sort(int[] arr) {
        System.out.println("using quick sort");
        quicksort(arr,0, arr.length-1);
        return arr;
    }

    public void quicksort(int[] arr, int start, int end){

        if(start >= end) return;

        int pivot = arr[end];

        int left = start;
        int right = end-1;

        while(left<=right){
            if(arr[left]<=pivot) {
                left++;
            } else {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                right--;
            }
        }

        arr[end] = arr[left];
        arr[left] = pivot;

        quicksort(arr, start, left-1);
        quicksort(arr, left+1, end);
    }

}(int[] arr, int start, int end){

        if(start >= end) return;

        int pivot = arr[end];

        int left = start;
        int right = end-1;

        while(left<=right){
            if(arr[left]<=pivot) {
                left++;
            } else {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                right--;
            }
        }

        arr[end] = arr[left];
        arr[left] = pivot;

        quicksort(arr, start, left-1);
        quicksort(arr, left+1, end);
    }

}
