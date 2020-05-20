# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:
# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:
# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:
# 输入: [1,3,5,6], 0
# 输出: 0


class Solution:
    # 48ms, 43.32%; 14.1MB, 7.14%
    def searchInsert(self, nums, target):
        if nums == []: return 0
        for index, value in enumerate(nums):
            if value >= target: return index
        return index+1

    # 二分法
    # 36ms, 90.10%; 14.3MB, 7.14%
    def searchInsert1(self, nums, target):
        if not nums:
            return 0
        if target in nums:
            return nums.index(target)
        left = 0
        right = len(nums) - 1
        if target > nums[right]: return right+1
        if target < nums[left]: return 0
        while left < right:
            mid = int(left + (right - left)/2)
            if nums[mid] > target:
                right = mid
            else:
                left = mid
            if right-left == 1: return right
        return left

    #44ms, 59.16%; 14.3MB, 7.14%
    def searchInsert2(self, nums, target):
        if target>nums[-1]:
            return len(nums)
        l,r = 0, len(nums)-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>=target:
                r = mid-1
                ans = mid
            else:
                l = mid+1
        return ans


if __name__ == "__main__":
    print(Solution().searchInsert1([1,3,5], 1))