# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
# 
# 示例 1:
# 给定 nums = [3,2,2,3], val = 3,
# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
# 给定 nums = [0,1,2,2,3,0,4,2], val = 2,
# 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
# 注意这五个元素可为任意顺序。
# 你不需要考虑数组中超出新长度后面的元素。


class Solution:
    # 32ms, 93.80%; 13.7MB, 7.14%
    def removeElement(self, nums, val):
        if not nums: return 0
        location = 0
        for index, value in enumerate(nums):
            if value != val:
                nums[location] = value
                location += 1

        print(nums)
        return location

    # 48ms, 26.74%; 13.8MB, 7.14%
    def removeElement1(self, nums, val):
        if not nums: return 0
        location = 0
        for value in nums:
            if value != val:
                nums[location] = value
                location += 1

        print(nums)
        return location

    # 40ms, 64.22%; 13.5MB, 7.14%
    def removeElement2(self, nums, val):
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        
        return n


if __name__ == "__main__":
    print(Solution().removeElement2([0,1,2,2,3,0,4,2], 2))