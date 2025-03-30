class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        arr.sort(key=lambda num: (abs(num-x),num))
        res=arr[:k]
        res.sort()
        return res
        
