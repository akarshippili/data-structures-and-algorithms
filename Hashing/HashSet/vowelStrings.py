class Solution:
    def __init__(self):
        self.vowles = set(['a', 'e', 'i', 'o', 'u'])
        
    def isVowelString(self, word):
        return word[0] in self.vowles and word[-1] in self.vowles
    
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum(list(map(self.isVowelString, words[left:right+1])))
        
