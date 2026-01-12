#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        length = len(nums)
        while fast < length:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


# @lc code=end


# ==========================================
# 调试测试代码
# ==========================================
if __name__ == "__main__":
    # 创建Solution实例
    sol = Solution()

    # 测试用例1: 示例用例
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = sol.removeElement(nums1, val1)
    print(f"测试1: nums={nums1}, val={val1}")
    print(f"  返回长度: {k1}, 修改后数组前{k1}项: {nums1[:k1]}")
    print("  预期: 长度=2, 前两项=[2, 2]\n")

    # 测试用例2: 示例用例
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = sol.removeElement(nums2, val2)
    print(f"测试2: nums={nums2}, val={val2}")
    print(f"  返回长度: {k2}, 修改后数组前{k2}项: {nums2[:k2]}")
    print("  预期: 长度=5, 前五项=[0, 1, 3, 0, 4]\n")

    # 测试用例3: 空数组
    nums3 = []
    val3 = 1
    k3 = sol.removeElement(nums3, val3)
    print(f"测试3: nums={nums3}, val={val3}")
    print(f"  返回长度: {k3}")
    print("  预期: 长度=0\n")

    # 测试用例4: 所有元素都需要移除
    nums4 = [1, 1, 1]
    val4 = 1
    k4 = sol.removeElement(nums4, val4)
    print(f"测试4: nums={nums4}, val={val4}")
    print(f"  返回长度: {k4}")
    print("  预期: 长度=0\n")

    # 测试用例5: 无需移除任何元素
    nums5 = [1, 2, 3]
    val5 = 4
    k5 = sol.removeElement(nums5, val5)
    print(f"测试5: nums={nums5}, val={val5}")
    print(f"  返回长度: {k5}, 修改后数组前{k5}项: {nums5[:k5]}")
    print("  预期: 长度=3, 前三项=[1, 2, 3]\n")
