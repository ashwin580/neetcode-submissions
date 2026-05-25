class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap= {}

        for i,num in enumerate(nums):

            difference = target - num

            if difference in hashmap and hashmap[difference] != i:
                return [hashmap[difference],i]
            
            hashmap[num] = i
        

        