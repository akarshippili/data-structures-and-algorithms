class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        
        winner = set()
        runner = set()
        lossers = set()
        
        visited = set()
        
        for w, r in matches:
            
            if(w not in visited): winner.add(w)
            
            if(r not in visited): 
                runner.add(r)
            elif(r in winner): 
                winner.remove(r)
                runner.add(r)
            elif(r in runner):
                runner.remove(r)
                lossers.add(r)
                
            
            visited.add(w)
            visited.add(r)        
        
        return [sorted([i for i in winner]), sorted([i for i in runner])]
