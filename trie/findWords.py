class TrieNode:
    def __init__(self):
        self.childern = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
    

    def add(self, word):
        node = self.root
        index = 0

        while(index<len(word)):
            idx = word[index]
            if(idx not in node.childern): node.childern[idx] = TrieNode()
            node = node.childern[idx]
            index += 1
        
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        N = len(board)
        M = len(board[0])

        dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        def dfs(rowIndex, colIndex, node):
            if(not node): return
            if(rowIndex<0 or rowIndex>=N or colIndex<0 or colIndex>=M or board[rowIndex][colIndex] == '.'): return

            ch = board[rowIndex][colIndex]
            if(ch not in node.childern): return

            parent = node
            node = node.childern[ch]
            if('$' in node.childern):
                ans.add(node.childern['$'].word[:-1])
                del node.childern['$']

            board[rowIndex][colIndex] = '.'            
            for dx, dy in dir:
                newx, newy = rowIndex + dx, colIndex + dy
                dfs(newx, newy, node)
                if(len(node.childern) == 0):
                    del parent.childern[ch]
                    break
            board[rowIndex][colIndex] = ch

            

        trie = Trie()
        for word in words: trie.add(word+'$')
        ans = set()

        for rowIndex in range(N):
            for colIndex in range(M):
                dfs(rowIndex, colIndex, trie.root)
        
        return list(ans)
