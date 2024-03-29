type Comparable[T any] interface {
	// 	if == returns 0
	// 	else if > returns 1
	// 	else return -1
	Compare(val T) int
}

type Heapable[T any] interface {
	Comparable[T]
	GetMin() T
	GetIndex() int
	SetIndex(index int)
}

type Heap[T Heapable[T]] struct {
	size int
	arr  []T
}

func GetHeap[T Heapable[T]]() *Heap[T] {
	heap := Heap[T]{
		size: 0,
		arr:  make([]T, 0),
	}

	return &heap
}

// Heap Operatrions
func (heap *Heap[T]) Add(val T) {
	// add element tio heap

	val.SetIndex(heap.size)
	if heap.size < len(heap.arr) {
		heap.arr[heap.size] = val
	} else {
		heap.arr = append(heap.arr, val)
	}
	heap.size += 1

	// shift to restore heap
	heap.HepifyUp(heap.size - 1)
}

func (heap *Heap[T]) Peek() (*T, error) {
	if heap.IsEmpty() {
		return nil, errors.New("invalid operation: heap is empty")
	}

	return &(heap.arr[0]), nil
}

func (heap *Heap[T]) Pop() (*T, error) {
	if heap.IsEmpty() {
		return nil, errors.New("invalid operation: heap is empty")
	}

	heap.Swap(0, heap.size-1)
	heap.size -= 1

	// shift to restore heap
	heap.HepifyDown(0)
	return &heap.arr[heap.size], nil
}

func (heap *Heap[T]) DecreaseKey(index int) error {
	if index >= heap.size {
		return errors.New("index out of bound")
	}

	heap.arr[index] = heap.arr[index].GetMin()
	heap.HepifyUp(index)
	return nil
}

func (heap *Heap[T]) DecreaseKeyWith(index int, new T) error {
	if index >= heap.size {
		return errors.New("index out of bound")
	}

	if heap.arr[index].Compare(new) != 1 {
		return errors.New("updating value should be less than the current")
	}

	heap.arr[index] = new
	heap.HepifyUp(index)
	return nil
}

func (heap *Heap[T]) IncreaseKeyWith(index int, new T) error {
	if index >= heap.size {
		return errors.New("index out of bound")
	}

	if heap.arr[index].Compare(new) != -1 {
		return errors.New("updating value should be greater than the current")
	}

	heap.arr[index] = new
	heap.HepifyDown(index)
	return nil
}

func (heap *Heap[T]) Delete(index int) error {
	if index >= heap.size {
		return errors.New("index out of bound")
	}

	heap.DecreaseKey(index)
	heap.Pop()
	return nil
}

func (heap *Heap[T]) IsEmpty() bool {
	return heap.size == 0
}

func (heap *Heap[T]) GetNumOfElements() int {
	return heap.size
}

// Helper Functions
func (heap *Heap[T]) Swap(index1 int, index2 int) error {
	if index1 >= heap.size {
		return errors.New("index1 is out of bound")
	}

	if index2 >= heap.size {
		return errors.New("index1 is out of bound")
	}

	heap.arr[index1], heap.arr[index2] = heap.arr[index2], heap.arr[index1]
	heap.arr[index1].SetIndex(index1)
	heap.arr[index2].SetIndex(index2)
	return nil
}

// shift-up to restore heap
func (heap *Heap[T]) HepifyUp(index int) {
	parentIndex := GetParentIndex(index)
	if heap.arr[index].Compare(heap.arr[parentIndex]) >= 0 {
		return
	}

	// swap
	heap.Swap(index, parentIndex)
	heap.HepifyUp(parentIndex)
}

// shift-down to restore heap
func (heap *Heap[T]) HepifyDown(index int) {
	smallest := index
	leftChildIndex := GetLeftChildIndex(index)
	rightChildIndex := GetRightChildIndex(index)

	if leftChildIndex < heap.size && heap.arr[smallest].Compare(heap.arr[leftChildIndex]) == 1 {
		smallest = leftChildIndex
	}

	if rightChildIndex < heap.size && heap.arr[smallest].Compare(heap.arr[rightChildIndex]) == 1 {
		smallest = rightChildIndex
	}

	if smallest == index {
		// if already in correct position
		return
	}

	// swap parant with smallest child
	heap.Swap(index, smallest)
	heap.HepifyDown(smallest)
}

func GetParentIndex(index int) int {
	return (index - 1) / 2
}

func GetLeftChildIndex(index int) int {
	return 2*index + 1
}

func GetRightChildIndex(index int) int {
	return 2*index + 2
}

type HeapInt struct {
	val int
}

func (s1 HeapInt) Compare(s2 HeapInt) int {

	if s1.val == s2.val {
		return 0
	} else if s1.val > s2.val {
		return 1
	}

	return -1
}

func (s HeapInt) GetMin() HeapInt {
	return GetHeapInt(-2147483648)
}

func (s HeapInt) GetIndex() int {
	return -1
}

func (s HeapInt) SetIndex(index int) {}

func GetHeapInt(s int) HeapInt {
	return HeapInt{
		val: s,
	}
}

func findKthLargest(nums []int, k int) int {
	heap := heap.GetHeap[HeapInt]()
	index := 0
	N := len(nums)

	for index < N {
		new := GetHeapInt(nums[index])

		peekpeek, _ := heap.Peek()
		if heap.GetNumOfElements() < k || (*peekpeek).Compare(new) == -1 {
			heap.Add(new)
		}

		if heap.GetNumOfElements() > k {
			heap.Pop()
		}

		index += 1
	}

	peekpeek, _ := heap.Peek()
	return (*peekpeek).val
}

func main() {
	nums := []int{3, 2, 1, 5, 6, 4}
	fmt.Println(findKthLargest(nums, 2))
}
