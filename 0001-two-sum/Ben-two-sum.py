class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums)-1):
            k = i + 1
            while k < len(nums):
                if nums[i] + nums[k] == target:
                    return [i,k]
                k+=1

        