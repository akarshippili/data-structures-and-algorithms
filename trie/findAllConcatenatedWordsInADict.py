class TrieNode:
    def __init__(self) -> None:
        self.children = [None for i in range(26)]
        self.isWord = False

class Trie:

    def __init__(self) -> None:
        self. root = TrieNode()
    
    def insert(self, x):
        node = self.root
        
        for ch in x:
            if(not node.children[ord(ch) - 97]): node.children[ord(ch) - 97] = TrieNode()
            node = node.children[ord(ch) - 97]

        node.isWord = True


    def containsWord(self, word):
        node = self.root
        
        for ch in word:
            if(not node.children[ord(ch) - 97]): return False
            node = node.children[ord(ch) - 97]

        return node.isWord
 

    def startsWith(self, prefix):
        arr = [] 

        def dfs(cur, node):
            if(not node): return
            
            if(node.isWord): arr.append(cur)
            for i in range(26):
                dfs(cur + chr(97+i), node.children[i])

        temp =  self.root
        for ch in prefix:
            if(not temp.children[ord(ch) - 97]): return
            temp = temp.children[ord(ch) - 97]
        
        dfs(prefix, temp)
        return arr


class Solution:

    def isConcatWord(self, word, trie, count):
        if((not word or word == '') and count>=2): return True
        
        root = trie.root
        for index in range(len(word)):
            ch = word[index]
            root = root.children[ord(ch) - 97]
            if(not root): return False
            if(root.isWord and self.isConcatWord(word[index+1:], trie, count+1)): return True
        
        return False


    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words: trie.insert(word)

        ans  = []
        for word in words:
            if(self.isConcatWord(word, trie, 0)):
                ans.append(word)
        
        return ans



        
