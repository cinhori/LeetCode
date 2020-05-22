# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 输入为非空字符串且只包含数字1和0。
# 
# 示例1:
# 输入: a = "11", b = "1"
# 输出: "100"
# 示例2:
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
# 提示：
# 每个字符串仅由字符'0'或'1'组成。
# 1 <= a.length, b.length <= 10 ^ 4
# 字符串如果不是"0" ，就都不含前导零。


class Solution:
    # 48ms, 43.87%; 13.6MB, 6.25%
    def addBinary(self, a, b):
        return self._addBinary(a, b, 0)

    # 递归
    def _addBinary(self, a, b, step):
        if a == '' and b == '':
            if step == 1:
                return '1'
            else:
                return ''
        if a == '': 
            temp = int(b[-1]) + step
            if temp >= 2:
                return self._addBinary('', b[0:-1], 1)+str(temp-2)
            else:
                return self._addBinary('', b[0:-1], 0)+str(temp)
        elif b == '': 
            temp = int(a[-1]) + step
            if temp >= 2:
                return self._addBinary(a[0:-1], '', 1)+str(temp-2)
            else:
                return self._addBinary(a[0:-1], '', 0)+str(temp)
        else:
            temp = int(a[-1]) + int(b[-1]) + step
            if temp >= 2:
                return self._addBinary(a[0:-1], b[0:-1], 1)+str(temp-2)
            else:
                return self._addBinary(a[0:-1], b[0:-1], 0)+str(temp)

    # 先计算等长段结果，后计算剩余段结果
    # 44ms, 61.98%; 13.7MB, 6.25%
    def addBinary2(self, a, b):
        min_len = len(a) if len(a) <= len(b) else len(b)
        border = 0 - min_len - 1
        step = 0
        result = ''
        for i in range(-1, border, -1):
            temp = int(a[i]) + int(b[i]) + step
            if temp >= 2:
                step = 1
                result = str(temp-2) + result
            else:
                step = 0
                result = str(temp) + result
        
        left = ''
        if len(a) > min_len:
            left = a
        elif len(b) > min_len:
            left = b
        if left == '':
            if step == 1:
                return '1'+result
            else:
                return result
        else:
            for i in range(0-(min_len+1), 0-(len(left)+1), -1):
                temp = int(left[i]) + step
                if temp >= 2:
                    step = 1
                    result = str(temp-2) + result
                else:
                    step = 0
                    result = str(temp) + result
        
        if step == 1:
            return '1'+result
        else:
            return result

    # 40ms, 78.71%; 13.7MB, 6.25%
    def addBinary3(self, a, b):
        return '{0:b}'.format(int(a, 2) + int(b, 2))

    # 36ms, 90.51%; 13.7MB, 6.25%
    def addBinary4(self, a, b):
        max_len = max(len(a), len(b))
        # Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0
        a, b = a.zfill(max_len), b.zfill(max_len)
        carry = 0
        result = ''

        for i in range(max_len-1, -1, -1):
            if a[i] == '1': carry += 1
            if b[i] == '1': carry += 1
            result += str(carry%2)
            carry = carry // 2

        if carry == 1:
            result += '1'
        print(result)
        return result[::-1]

    # 位操作
    # 40ms, 78.89%; 13.8MB, 6.25%
    def addBinary5(self, a, b):
        x, y = int(a, 2), int(b, 2)
        while y != 0:
            result = x ^ y
            carry = (x & y) << 1
            x, y = result, carry

        # bin(10) == '0b1010'
        return bin(x)[2:]


if __name__ == "__main__":
    print(Solution().addBinary5('1010', '1011'))