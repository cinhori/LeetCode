#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Easy (41.53%)
# Likes:    583
# Dislikes: 0
# Total Accepted:    130.3K
# Total Submissions: 312.7K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 
# 
# 示例 2:
# 
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 
# 说明:
# 
# 
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
# 
# 
#

# @lc code=start
class Solution:
    # # time limit exceeded
    # # 暴力求解，每次移动一位
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     for _ in range(k):
    #         temp = nums[-1]
    #         for i in range(len(nums)-2, -1, -1):
    #             nums[i+1] = nums[i]
    #         nums[0] = temp

    # # 44ms, 64.93%; 14MB, 70.27%
    # # 借助额外空间，完成后拷贝
    # def rotate(self, nums: List[int], k: int) -> None:
    #     lens = len(nums)
    #     temp = nums[lens-k:lens] + nums[0:(lens-k)]
    #     # print(temp)
    #     for i in range(lens):
    #         nums[i] = temp[i]

    # # 40ms, 81.27%; 13.8MB, 100%
    # # 环状替换，直接将每个元素拷贝到目的位置
    # def rotate(self, nums: List[int], k: int) -> None:
    #     k = k % len(nums)
    #     lens = len(nums)
    #     count = 0
    #     for start in range(len(nums)):
    #         current = start
    #         pre = nums[start]
    #         while True:
    #             next_location = (current + k) % lens
    #             temp = nums[next_location]
    #             nums[next_location] = pre
    #             current = next_location
    #             pre = temp
    #             count += 1
    #             if start == current: break
    #         if count == lens:
    #             return

    # 44ms, 65.03%; 13.9MB, 94.59%
    # 反转
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

# @lc code=end

