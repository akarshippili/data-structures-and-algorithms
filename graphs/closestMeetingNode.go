func min(a int, b int) int{
    if(a>b){
        return b
    }

    return a
}

func closestMeetingNode(edges []int, node1 int, node2 int) int {

    n := len(edges)
    visited1 := make([]bool, n)
    visited2 := make([]bool, n)
    found := 1000000001

    visited1[node1] = true
    visited2[node2] = true


    for node1 != -1 || node2 != -1 {

        if(node2!=-1 && visited1[node2]){
            found = min(found, node2)
        }

        if(node1 != -1 && visited2[node1]){
            found = min(found, node1)
        }

        if(found != 1000000001){
            return found
        }

        if(node1 != -1){
            node1 = edges[node1]
        }

        if(node2 != -1){
            node2 = edges[node2]
        }

        if(node1!=-1 && visited1[node1]){
            node1 = -1
        }

        if(node2!=-1 && visited2[node2]){
            node2 = -1
        } 

        if(node1!=-1){
            visited1[node1] = true
        }

        if(node2!=-1){
            visited2[node2] = true
        }

    }
    
    return -1
}
