package com.akarsh.codechef.segmentTree;

import java.util.Arrays;

public class SegmentTree<T extends Number> {

    private final int n;
    private final double[] segmentTree;
    private final T[] arr;

    SegmentTree(int n, T[] arr){
        this.n = n;
        int modifiedChildCount = (int) Math.pow(2, Math.ceil(Math.log(n)/Math.log(2)));
        int size = 2 * modifiedChildCount - 1;
        this.segmentTree = new double[size];
        this.arr = arr;
        buildSegmentTree(arr);
    }

    public void buildSegmentTree(T[] arr){
        helper(0, arr.length-1, 0);
    }

    public void helper(int start, int end, int index){

        if(start == end){
            this.segmentTree[index] = arr[start].doubleValue();
            return;
        }

        int mid = start + (end - start)/2;
        helper(start, mid, 2*index + 1);
        helper(mid+1, end, 2*index + 2);
        this.segmentTree[index] = this.segmentTree[2*index+1] + this.segmentTree[2*index+2];
    }

    public void updateHelper(int start, int end, int arrIndex, int segIndex) {

        if(start == end){
            this.segmentTree[segIndex] = this.arr[arrIndex].doubleValue();
            return;
        }

        int mid = start + (end - start)/2;
        if(arrIndex <= mid) updateHelper(start, mid, arrIndex, segIndex*2 + 1);
        else updateHelper(mid+1, end, arrIndex, segIndex*2 + 2);

        this.segmentTree[segIndex] = this.segmentTree[2*segIndex+1] + this.segmentTree[2*segIndex+2];
    }

    public void update(int index, T newValue){
        this.arr[index] = newValue;
        updateHelper(0,n-1, index, 0);
    }

    public Double query(int start, int end){
        return query(start, end, 0, n-1,0);
    }

    private Double query(int start, int end, int vStart, int vEnd, int index){

        System.out.println(start + " " + end + " " + vStart + " " + vEnd + " " + index);
        if(start>end) return 0.0;

        if(start == vStart && end == vEnd) return segmentTree[index];
        if(start>vEnd || end<vStart) return 0.0;

        int mid = vStart + (vEnd - vStart)/2;

        if(end<=mid) return query(start, end, vStart, mid, 2*index+1);
        if(start>mid) return query(start, end, mid+1, vEnd, 2*index+2);

        return query(start, mid, vStart, mid, 2*index+1) +  query(mid+1, end, mid+1, vEnd, 2*index+2);
    }



    @Override
    public String toString() {
        return "SegmentTree{" +
                "segmentTree=" + Arrays.toString(segmentTree) +
                ", arr=" + Arrays.toString(arr) +
                '}';
    }
}
