class TrieNode:
    
    def __init__(self):
        self.childern = [None for _ in range(26)]
        self.set = set()


class Solution:
    def countPrefixSuffixPairs(self, words) -> int:
        
        self.prefix_root = TrieNode()
        self.suffix_root = TrieNode()
        ans = 0
        
        for index, word in enumerate(words):            
            temp = self.prefix_root
            s1 = set()
            s1 = s1.union(temp.set)
            
            for ch in word:
                if(temp.childern[ord(ch) - 97] == None): temp.childern[ord(ch) - 97] = TrieNode()
                temp = temp.childern[ord(ch) - 97]
                s1 = s1.union(temp.set)
                
            
            temp.set.add(index)
            
            
            temp = self.suffix_root
            s2 = set()
            s2 = s2.union(temp.set)

            for ch in word[::-1]:
                if(temp.childern[ord(ch) - 97] == None): temp.childern[ord(ch) - 97] = TrieNode()
                temp = temp.childern[ord(ch) - 97]
                s2 = s2.union(temp.set)

        
            temp.set.add(index)
            ans += len(s1.intersection(s2))
        
        return ans


s = Solution()
ans = s.countPrefixSuffixPairs(["a","aba","ababa","aa"])
print(ans)     