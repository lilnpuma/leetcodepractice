class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s= len(nums)
        for i in range(s):
            for j in range(s):
                if j == s-1:
                    break
                elif i == j+1:
                    break
                elif (nums[i] + nums[j+1]) == target:
                    return[i,j+1]
            
