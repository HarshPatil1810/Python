class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)

        if n==1:
            return nums[0]

        dist_collection=list(set(nums))
        dist_collection.sort();
        if len(dist_collection) >=3:
            return dist_collection[-3];
        else:
           return  dist_collection[-1]
