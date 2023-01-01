class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(" ")
        if(len(pattern) != len(arr)): return False

        mapper = {}
        visited = set()

        for index in range(len(arr)):
            if(pattern[index] in mapper and mapper[pattern[index]] != arr[index]): 
                return False
            elif(pattern[index] in mapper): 
                continue
            else:
                if(arr[index] in visited): return False
                mapper[pattern[index]] = arr[index]
                visited.add(arr[index])

        return True
