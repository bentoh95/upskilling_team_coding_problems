class Solution(object):
    def majorityElement(self, nums):
        dict = {}
        for n in nums:
            if n in dict:
                dict[n] += 1
            if n not in dict:
                dict[n] = 0
                
        largest_occurence = -1
        ans = -1
        for key, value in dict.items():
            if value > largest_occurence:
                largest_occurence = value
                ans = key
        return ans

        