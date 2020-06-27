#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
# https://leetcode-cn.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (61.52%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    42.8K
# Total Submissions: 69.2K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n' +
  '[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
# 
# 示例：
# 
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 说明:
# 
# 
# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。
# 
# 
#

# @lc code=start
class NumArray:
    # 96ms, 87.51%; 17.5MB, 17.24%
    def __init__(self, nums: List[int]):
      self.nums_sum = [nums[0]] if nums else None
      for i in range(1, len(nums)):
        self.nums_sum.append(self.nums_sum[i-1] + nums[i])
        
    def sumRange(self, i: int, j: int) -> int:
      if not self.nums_sum: return None 
      return self.nums_sum[j]-self.nums_sum[i-1] if i>=1 else self.nums_sum[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

