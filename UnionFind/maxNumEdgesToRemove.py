from SimilarStringGroups import UnionFind


class Solution:
    def maxNumEdgesToRemove(self, n, edges):

        alice = UnionFind(n)
        count = 0
        numEdges = len(edges)

        for edgeType, source, dest in edges:
            if(edgeType == 3):
                alice.merge(source-1, dest-1)
                count += 1
                if(alice.getNumberOfComponents() == 1): return numEdges - count

        bob = alice.clone()

        graph = [alice, bob]

        for edgeType, source, dest in edges:
            if(edgeType == 3): continue
            if(edgeType == 1 and alice.areConnected(source-1, dest-1)): continue 
            if(edgeType == 2 and bob.areConnected(source-1, dest-1)): continue
            
            graph[edgeType].merge(source-1, dest-1)
            count += 1
            if(alice.getNumberOfComponents() == 1 and bob.getNumberOfComponents() == 1): return numEdges - count
        
        return -1