#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
# https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (53.85%)
# Likes:    298
# Dislikes: 0
# Total Accepted:    96.3K
# Total Submissions: 178.2K
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
# 
# 说明:
# 
# 
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 
# 
# 示例:
# 
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
# 
#

# @lc code=start
class Solution:
    # # 40ms, 88.5%; 14.2MB, 6.25%
    # # 双指针
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     i, j = 0, len(numbers)-1
    #     while i != j:
    #         if numbers[i] + numbers[j] == target:
    #             return [i+1, j+1]
    #         elif numbers[i] + numbers[j] > target:
    #             j -= 1
    #         else:
    #             i += 1
    #     return None

    # 48ms, 54.46%; 14MB, 6.25%
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i

# @lc code=end

