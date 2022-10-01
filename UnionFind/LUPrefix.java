class LUPrefix {

    UnionFind uf;
    boolean[] uploaded;
    
    public LUPrefix(int n) {
        uf = new UnionFind(n+1);
        uploaded = new boolean[n+1];
    }
    
    public void upload(int video) {
        
        if(video>0 && uploaded[video-1]) uf.merge(video, video-1);
        if(video<uploaded.length-1 && uploaded[video+1]) uf.merge(video, video+1);
        
        uploaded[video] = true;
    }
    
    public int longest() {
        return uploaded[1] ? uf.componentSize(1) :  0;
    }
}

