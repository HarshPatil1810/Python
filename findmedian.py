class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        merge=nums1+nums2
        merge.sort()
        length=len(merge)

        if length % 2==0:
            med=(merge[length//2-1]+merge[length//2])/2.0
        else:
            med=(merge[length//2])

        return med
        
