class MyCircularQueue {

    private int size;
    private int capacity;
    private Node head;
    private Node tail;
    
    
    public MyCircularQueue(int k) {
        this.size = 0;
        this.capacity = k;
    }
    
    public boolean enQueue(int value) {
        if(capacity <= size) return false;
        
        if(tail == null){
            head = tail = new Node(value, null, null);
            size++;
        } else {
            Node newNode = new Node(value, tail, null);
            tail.next = newNode;
            tail = tail.next;
            size++;
        }
        
        return true;
    }
    
    public boolean deQueue() {
        if(isEmpty()) return false;
                
        head = head.next;
        size--;
        if(size == 0) tail = null;
        return true;
    }
    
    public int Front() {
        if(head == null) return -1;
        return head.val;
    }
    
    public int Rear() {
        if(tail == null) return -1;
        return tail.val;
    }
    
    public boolean isEmpty() {
        return size == 0;
    }
    
    public boolean isFull() {
        return size == capacity;
    }
}

class Node{
    int val;
    Node prev;
    Node next;
    
    public Node(int val){
        this.val = val;
    }
    
    public Node(int val, Node prev, Node next){
        this.val = val;
        this.prev = prev;
        this.next = next;
    }
}



/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
