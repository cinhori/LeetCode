#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (47.72%)
# Likes:    509
# Dislikes: 0
# Total Accepted:    150.4K
# Total Submissions: 315.2K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 
# 
# 
# 说明:
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 
# 
# 示例:
# 
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6]
# 
#

# @lc code=start
class Solution:
    # 32ms, 96.11%; 13.7MB, 6.9%
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # def merge(self, nums1, m, nums2, n):

        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return None
        pointer = m + n - 1
        pointer_nums1 = m - 1
        pointer_nums2 = n - 1
        while pointer_nums2 != -1 and pointer_nums1 != -1:
            if nums2[pointer_nums2] > nums1[pointer_nums1]:
                nums1[pointer] = nums2[pointer_nums2]
                pointer -= 1
                pointer_nums2 -= 1
            else:
                nums1[pointer] = nums1[pointer_nums1]
                pointer_nums1 -= 1
                pointer -= 1
        if pointer_nums1 == -1:
            while pointer_nums2 != -1:
                nums1[pointer] = nums2[pointer_nums2]
                pointer_nums2 -= 1
                pointer -= 1

# if __name__ == "__main__":
    # nums1 =[1,5,7,0,0]
    # Solution().merge(nums1, 3, [2,5], 2)
    # print(nums1)
# @lc code=end

