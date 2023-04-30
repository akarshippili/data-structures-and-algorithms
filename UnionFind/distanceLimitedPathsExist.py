from SimilarStringGroups import UnionFind

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList, queries):

        for index, query in enumerate(queries): query.append(index)
        queries.sort(key = lambda x: x[2])
        uf = UnionFind(n)
        index = 0
        queriesLength = len(queries)
        ans = [None for i in range(queriesLength)]

        edgeList.sort(key = lambda x: x[-1])
        edgesLength = len(edgeList)
        edgesIndex = 0

        while(index < queriesLength):
            source, dest, limit, qindex = queries[index]
            while(edgesIndex<edgesLength and edgeList[edgesIndex][-1]<limit):
                uf.merge(edgeList[edgesIndex][0], edgeList[edgesIndex][1])
                edgesIndex += 1
            ans[qindex] = uf.areConnected(source, dest)
            index += 1
        
        return ans