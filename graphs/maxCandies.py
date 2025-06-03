class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        queue = collections.deque()

        for box in initialBoxes:
            if status[box] == 1: queue.append(box)
            else: status[box] = 2

        candies_found = 0

        while(queue):
            box_index = queue.popleft()
            if status[box_index] == 4: continue

            candies_found += candies[box_index]
            status[(box_index)] = 4

            for key in keys[box_index]:
                if status[key] == 0: status[key] = 1
                if status[key] == 2: queue.append(key)
            
            for new_box in containedBoxes[box_index]:
                if status[new_box] == 4: continue
                if status[new_box] == 1: queue.append(new_box)
                else: status[new_box] = 2
        
        # print(processed, visited, keys_found, candies_found)
        return candies_found