type UinonFind struct {
	size          int
	numComponents int
	id            []int
	sizes         []int
}

func GetUnionFind(size int) *UinonFind {
	uf := UinonFind{
		size:          size,
		numComponents: size,
		id:            make([]int, size),
		sizes:         make([]int, size),
	}

	for i := 0; i < size; i++ {
		uf.id[i] = i
		uf.sizes[i] = 1
	}
	return &uf
}

func (uf *UinonFind) Merge(index1 int, index2 int) {
	root1 := uf.Find(index1)
	root2 := uf.Find(index2)

	if root1 == root2 {
		return
	}

	if root1 <= root2 {
		uf.id[root2] = root1
		uf.sizes[root1] += uf.sizes[root2]
	} else {
		uf.id[root1] = root2
		uf.sizes[root2] += uf.sizes[root1]
	}

	uf.numComponents = uf.numComponents - 1
}

func (uf *UinonFind) Find(index int) int {

	root := index
	for root != uf.id[root] {
		root = uf.id[root]
	}

	for root != index {
		parent := uf.id[index]
		uf.id[index] = root
		index = parent
	}
	return root
}

func (uf *UinonFind) IsConnected(index1 int, index2 int) bool {
	return uf.Find(index1) == uf.Find(index2)
}

func (uf *UinonFind) GetSizeOfComp(index int) int {
	return uf.sizes[uf.Find(index)]
}

func (uf *UinonFind) GetSize() int {
	return uf.size
}

func (uf *UinonFind) GetNumOfComp() int {
	return uf.numComponents
}

func smallestEquivalentString(s1 string, s2 string, baseStr string) string {
    uf := GetUnionFind(26)
    for i:=0; i<len(s1); i++ {
        uf.Merge(int(s1[i])-97, int(s2[i])-97)       
    }

    chars := "abcdefghijklmnopqrstuvwxyz"
    ans := make([]byte, len(baseStr))
    for i:=0; i<len(baseStr); i++{
        ans[i] = chars[uf.Find(int(baseStr[i])-97)]
    }
    return string(ans)   
}
