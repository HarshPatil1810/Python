class Solution:
    def twoSum(self, nums, target):
       
        hm = {}
        
        
        for i in range(len(nums)):
            # Calculate the required number to meet the target
            req_num = target - nums[i]
            
          
            if req_num in hm:
                return [hm[req_num], i]
            
           
            hm[nums[i]] = i
        
       
        return None


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))  # Output: [0, 1]
