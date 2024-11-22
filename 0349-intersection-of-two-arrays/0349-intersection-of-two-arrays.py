class Solution(object):
    def intersection(self, nums1, nums2):
        h=set()
        for i in nums1:
            h.add(i)
        
        ans=set()
        for i in nums2:
            if i in h:
                ans.add(i)
        
        return list(ans)
                
            

        