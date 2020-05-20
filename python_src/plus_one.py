# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 示例 1:
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。


class Solution:
    # 40ms, 64.32%; 13.6MB, 6.82%
    def plusOne(self, digits):
        if digits == []: return []
        digits[-1] += 1
        lens = 0-len(digits)
        for i in range(-1, lens, -1):
            if digits[i] == 10:
                digits[i-1] += 1
                digits[i] = 0
            else:
                break
        
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        else: 
            return digits

    # 40ms, 64.32%; 13.7MB, 6.82%
    def plusOne1(self, digits):
        pointer = len(digits)-1
        while(pointer != -1):
            if digits[pointer] != 9:
                digits[pointer] += 1
                return digits
            else:
                digits[pointer] = 0
                pointer -= 1
        return [1]+digits


    
if __name__ == "__main__":
    print(Solution().plusOne1([9,9,9]))
