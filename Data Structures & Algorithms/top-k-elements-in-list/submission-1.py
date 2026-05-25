class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency_map = {}

        for num in nums:
            frequency_map[num] = 1 + frequency_map.get(num, 0)
        
        frequency_map = dict(sorted(frequency_map.items(), key = lambda x: x[1], reverse=True))

        k_element = list(frequency_map.items())[:k]

        return [key[0] for key in k_element]
        