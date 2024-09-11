class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minh=[]
        for num in nums:
            heapq.heappush(minh,num)

            if len(minh) > k:
                heapq.heappop(minh)

    
        return minh[0]


        
