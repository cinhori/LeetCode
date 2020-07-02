#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (48.33%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    92.8K
# Total Submissions: 189.9K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
# 
# 示例 1:
# 
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
# 
# 
# 示例 2:
# 
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
# 
# 说明：
# 
# 
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
# 
# 
# 进阶:
# 
# 
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
# 
# 
#

# @lc code=start
class Solution:
    # 108ms, 10.03%; 14MB, 12.5%
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     dict1, dict2, set1, set2 = {}, {}, set(nums1), set(nums2)
    #     for i in set1:
    #         count = nums1.count(i)
    #         if count in dict1:
    #             dict1[count].append(i)
    #         else:
    #             dict1[count] = [i]
    #     for i in set2:
    #         count = nums2.count(i)
    #         if count in dict2:
    #             dict2[count].append(i)
    #         else:
    #             dict2[count] = [i]
    #     res = []
    #     for i in dict1:
    #         for j in dict2:
    #             res += list(set(dict1[i]) & set(dict2[j])) * min(i, j)
    #     return res

    # # 64ms, 64.38%; 13.7MB, 12.5%
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     dict, result = {}, []
    #     for i in nums1:
    #         dict[i] = dict.get(i, 0) + 1
    #     for i in nums2:
    #         if dict.get(i, 0) > 0:
    #             result.append(i)
    #             dict[i] -= 1
    #     return result

    # 60ms, 79.59%; 13.7MB, 12.5%
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        r = []
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] == nums2[right]:
                r.append(nums1[left])
                left += 1
                right += 1    
            else:
                right += 1
        return r

# @lc code=end

