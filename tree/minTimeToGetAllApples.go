func minTime(n int, edges [][]int, hasApple []bool) int {
    graph := make(map[int][]int)

    for _, edge := range edges{
        source := edge[0]
        dest := edge[1]

        graph[source] = append(graph[source], dest)
        graph[dest] = append(graph[dest], source)

    }
    ans,_ := helper(0, -1, hasApple, graph)
    return ans
}


func helper(node int, parent int, hasApple []bool, graph map[int][]int) (a int, has bool)  {
    ans := 0
    hasAppleInSubTree := hasApple[node]

    for _, child := range graph[node]{    
        if(child == parent){
            continue;
        }
        
        cur, has := helper(child, node, hasApple, graph)
        if(has){
            ans += cur + 2
            hasAppleInSubTree = true
        }
    }

    return ans, hasAppleInSubTree
