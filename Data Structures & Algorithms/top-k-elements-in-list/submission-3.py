class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        frequency_map = [[] for _ in range(len(nums)+1)]

        for n, c in count.items():
            frequency_map[c].append(n)
        
        res = []
        for i in range(len(frequency_map)-1,0,-1):
            for n in frequency_map[i]:
                res.append(n)
                if len(res) == k:
                    return res
        