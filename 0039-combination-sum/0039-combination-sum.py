class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        
        def dfs(i, curr, total):
            if total == target:
                copied_list = list(curr)  # Creates a shallow copy
                ans.append(copied_list)
                return
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            # recursively calls same number, left side of tree
            dfs(i, curr, total + candidates[i])
            curr.pop() # remove the current 
            dfs(i + 1, curr, total)
            
        dfs(0,[],0)
        return ans
            
            

            