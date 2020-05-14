# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
# 
# 示例 1:
# 给定数组 nums = [1,1,2], 
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
# 你不需要考虑数组中超出新长度后面的元素。

class Solution:
    # 52ms, 71.66%; 14.8MB, 8.16%
    def removeDuplicates(self, nums):
        if not nums: return 0
        location = 1
        data = nums[0]
        for index, value in enumerate(nums):
            if value > data:
                nums[location] = value
                location += 1
                data = value
        
        print(nums)
        return location

    # 48ms, 81.49%; 14.8MB, 8.16%
    def removeDuplicates2(self, nums):
        if not nums: return 0
        location = 1
        for index, value in enumerate(nums):
            if value > nums[location-1]:
                nums[location] = value
                location += 1
        
        print(nums)
        return location

    # 56ms, 64.20%; 14.7MB, 8.16%
    def removeDuplicates3(self, nums):
        if not nums: return 0
        i = 0 
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == "__main__":
    print(Solution().removeDuplicates2([1,1,2]))