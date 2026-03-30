class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #creating the set 
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            
            #tracking the number and index
            seen[nums[i]] = i