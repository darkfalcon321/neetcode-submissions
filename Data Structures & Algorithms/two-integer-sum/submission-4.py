class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        for i in range(len(nums) - 1):
            while start < end:
                if nums[start] + nums[end] == target:
                    a = []
                    a.append(start)
                    a.append(end)
                    return a
                    
                end-=1
            start +=1
            end = len(nums) - 1