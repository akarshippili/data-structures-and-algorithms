import java.util.Arrays;

public class Heap {

    private int[] heap;
    private int size;

    public Heap() {
        this.heap = new int[8];
        this.size = 0;
    }

    public Heap(int capacity) {
        this.heap = new int[capacity];
        this.size = 0;
    }

    private int getParentIndex(int index){
        return (index-1)/2;
    }

    private int getLeftChildIndex(int index){
        return 2*index + 1;
    }

    private int getRightChildIndex(int index){
        return 2*index + 2;
    }

    public int peek() {
        if(this.size==0) throw new IllegalStateException("size of heap is zero");
        return this.heap[0];
    }

     public int poll(){
        if(this.size==0) throw new IllegalStateException("size of heap is zero");
        swapElements(0, this.size-1);
        int val = this.heap[size-1];
        size--;
        heapifyDown();
        return val;
    }

    public void insert(int val){
        increaseSize();
        heap[size] = val;
        size++;
        heapifyUp();
    }

    private void heapifyUp() {
        int curIndex = this.size - 1;
        while (curIndex>0 && this.heap[getParentIndex(curIndex)] > this.heap[curIndex]) {
            swapElements(getParentIndex(curIndex), curIndex);
            curIndex = getParentIndex(curIndex);
        }
    }

    private void heapifyDown() {
        int curIndex = 0;

        while(true){
            int leftIndex = getLeftChildIndex(curIndex);
            int rightIndex = getRightChildIndex(curIndex);

            if(leftIndex>=this.size) return;

            int smallestIndex = curIndex;

            if(this.heap[curIndex]>this.heap[leftIndex]) smallestIndex = leftIndex;
            if(rightIndex<this.size && this.heap[smallestIndex]>this.heap[rightIndex]) smallestIndex = rightIndex;

            if(curIndex == smallestIndex) return;

            swapElements(curIndex, smallestIndex);
            curIndex = smallestIndex;
        }
    }

    private void heapifyDown(int index) {
        int curIndex = index;

        while(true){
            int leftIndex = getLeftChildIndex(curIndex);
            int rightIndex = getRightChildIndex(curIndex);

            if(leftIndex>=this.size) return;

            int smallestIndex = curIndex;

            if(this.heap[curIndex]>this.heap[leftIndex]) smallestIndex = leftIndex;
            if(rightIndex<this.size && this.heap[smallestIndex]>this.heap[rightIndex]) smallestIndex = rightIndex;

            if(curIndex == smallestIndex) return;

            swapElements(curIndex, smallestIndex);
            curIndex = smallestIndex;
        }
    }

    private void increaseSize() {
        if(size<heap.length) return;

        int curSize = heap.length;
        int[] arr = new int[2*curSize];
        System.arraycopy(heap, 0, arr, 0, curSize);
        heap = arr;
    }

    private void swapElements(int sourceIndex, int destinationIndex) {
        if(sourceIndex>=this.heap.length || destinationIndex>=this.heap.length) throw new IllegalStateException();

        int temp = this.heap[sourceIndex];
        this.heap[sourceIndex] = this.heap[destinationIndex];
        this.heap[destinationIndex] = temp;
    }

    @Override
    public String toString(){
        return Arrays.toString(this.heap);
    }

    public boolean isEmpty() {
        return this.size == 0;
    }
}
