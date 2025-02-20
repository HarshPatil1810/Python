class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = left + (right - left) // 2  # Corrected mid calculation
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    first = mid  # Store the first occurrence
            return first

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = left + (right - left) // 2  # Corrected mid calculation
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    last = mid  # Store the last occurrence
            return last

        first = findFirst(nums, target)
        last = findLast(nums, target)

        return [first, last]

# Example Usage
nums = [5, 7, 7, 8, 8, 10]
target = 8
sol = Solution()
print(sol.searchRange(nums, target))  # Output: [3, 4]
