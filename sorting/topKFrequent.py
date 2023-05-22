# using bucket sort -- O(n logk)
# another way it to use a heap of size k -- O(n)
# quickselect (loop this up) -- O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        N = len(nums)
        counter = defaultdict(int)
        for num in nums: counter[num] += 1

        buckets = [[] for i in range(N+1)]
        for key in counter: buckets[counter[key]].append(key)

        ans = []
        index = N
        count = k
        while(count>0):
            bucket = buckets[index]
            for i in bucket: ans.append(i)
            index -= 1
            count -= len(bucket)

        return ans[:k]
