func countSubTrees(n int, edges [][]int, labels string) []int {
    ans := make([]int, n)
    graph := make(map[int][]int)

    for _, edge := range edges{
        graph[edge[0]] = append(graph[edge[0]], edge[1])
        graph[edge[1]] = append(graph[edge[1]], edge[0])
    }
    // fmt.Println(graph)

    helper(0, -1, graph, &labels, &ans)
    return ans
}

func helper(node int, parent int, graph map[int][]int, ptrLabel *string, ans *[]int) []int {
    arr := make([]int, 26)
    for _, child := range graph[node]{
        if(child == parent){
            continue
        }

        childCur := helper(child, node, graph, ptrLabel, ans)
        add(&arr, childCur)
    }

    arr[ (*ptrLabel)[node] - 97 ] += 1
    (*ans)[node] = arr[ (*ptrLabel)[node] - 97 ]
    return arr
}

func add(arr1 *[]int, arr2 []int){
    for index, val := range arr2{
        (*arr1)[index] += val 
    }
}
