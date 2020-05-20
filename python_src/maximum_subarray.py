# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 进阶:
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


class Solution:
    # 动态规划
    #48ms, 76.96%; 14.3MB, 6.35%
    def maxSubArray(self, nums):
        if not nums: return None
        max = nums[0]
        now = nums[0]
        for i in range(1, len(nums)):
            # if nums[i] >= 0:
            #     if now >= 0:
            #         now += nums[i]
            #     else:
            #         now = nums[i]
            # else:
            #     if now < 0:
            #         now = nums[i]
            #     else:
            #         max = max if max > now else now
            #         now += nums[i]
            max = max if max > now else now
            if now < 0:
                now = nums[i]
            else:
                now += nums[i]
        return max if max > now else now

    #分治法
    # 我们定义一个操作 get(a, l, r) 表示查询a序列 [l, r]区间内的最大子段和，那么最终我们要求的答案就是 get(nums, 0, nums.size() - 1)。
    # 如何分治实现这个操作呢？对于一个区间 [l, r]，我们取 m = (l+r)//2，对区间[l,m]和[m+1,r] 分治求解。当递归逐层深入直到区间长度缩小为1的时候，递归「开始回升」。
    # 这个时候我们考虑如何通过[l,m]区间的信息和[m+1,r] 区间的信息合并成区间[l,r]的信息。最关键的两个问题是：
    # 我们要维护区间的哪些信息呢？
    # 我们如何合并这些信息呢？
    # 对于一个区间[l,r]，我们可以维护四个量：
    # lSum 表示 [l, r]内以l为左端点的最大子段和
    # rSum 表示 [l, r]内以r为右端点的最大子段和
    # mSum 表示 [l, r]内的最大子段和
    # iSum 表示 [l, r]的区间和
    # 以下简称[l,m]为[l, r]的「左子区间」，[m+1,r] 为 [l,r] 的「右子区间」。我们考虑如何维护这些量呢（如何通过左右子区间的信息合并得到[l,r]的信息）？
    # 对于长度为 11 的区间 [i, i][i,i]，四个量的值都和 a_i相等。对于长度大于1的区间：
    # 首先最好维护的是 iSum，区间[l,r] 的 iSum 就等于「左子区间」的 iSum 加上「右子区间」的 iSum。
    # 对于[l,r]的 lSum，存在两种可能，它要么等于「左子区间」的 lSum，要么等于「左子区间」的 iSum 加上「右子区间」的 lSum，二者取大。
    # 对于[l,r] 的 rSum，同理，它要么等于「右子区间」的 rSum，要么等于「右子区间」的 iSum 加上「左子区间」的 rSum，二者取大。
    # 当计算好上面的三个量之后，就很好计算[l,r]的mSum了。我们可以考虑[l,r]的mSum对应的区间是否跨越m——它可能不跨越m，也就是说[l,r] 的 mSum 可能是「左子区间」的 mSum 和 「右子区间」的 mSum 中的一个；它也可能跨越m，可能是「左子区间」的 rSum 和 「右子区间」的 lSum 求和。三者取大。
    # 96ms, 11.91%; 14.3MB, 6.35%
    def maxSubArray2(self, nums):
        return Solution()._get_status(nums, 0, len(nums)-1)[2]

    # [lsum, rsum, msum, isum]
    def _get_status(self, nums, l, r):
        if l == r: return [nums[l], nums[l],nums[l], nums[l]]
        m = (l+r)//2
        left_block = Solution()._get_status(nums, l, m)
        right_block = Solution()._get_status(nums, m+1, r)
        return [max(left_block[0], left_block[3]+right_block[0]), 
                max(right_block[1], right_block[3]+left_block[1]), 
                max(left_block[2], right_block[2], left_block[1]+right_block[0]), 
                left_block[3]+right_block[3]]


if __name__ == "__main__":
    # print(Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubArray([-2]))
