package com.akarsh.codechef.unionfind;

// ds which tracks elements of split into one or more disjoint group/sets


// primary operation:
// find -> returns which set the element belongs to
// union -> merges two sets


public class UnionFind {
    private int size; // number of elements in union find
    private int[] sz; // size of each component
    private int[] id; // id[idx] -> has parent index of idx
    private int numComponents;

    public UnionFind(int size){
        if(size<=0) throw new IllegalArgumentException("size should be greater than zero");
        this.size = size;
        this.numComponents = size;
        this.id = new int[size];
        this.sz = new int[size];

        for(int index=0; index<size; index++) {
            id[index] = index;
            sz[index] = 1;
        }
    }

    public int find(int index){
        int root = index;
        while(this.id[root] != root) root = this.id[root];

        while(index!=root){
            int temp = this.id[index];
            this.id[index] = root;
            index = temp;
        }
        return root;
    }

    public boolean isConnected(int index1, int index2){
        return find(index1) == find(index2);
    }

    public int componentSize(int index){
        return this.sz[find(index)];
    }

    public int getSize(){
        return this.size;
    }

    public int getNumComponents(){
        return this.numComponents;
    }

    public void merge(int index1, int index2){
        int root1 = find(index1);
        int root2 = find(index2);

        if(root1 == root2) return;


        if(this.sz[root1]<=this.sz[root2]){
            sz[root2] +=  sz[root1];
            id[root1] = root2;
        } else {
            sz[root1] +=  sz[root2];
            id[root2] = root1;
        }

        numComponents--;
    }

}
