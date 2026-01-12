#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#
from typing import List


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        length = len(nums)
        while fast < length:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


# @lc code=end


# ==========================================
# 调试测试代码
# ==========================================
if __name__ == "__main__":
    sol = Solution()

    # 测试用例1: 示例用例
    nums1 = [1, 1, 2]
    k1 = sol.removeDuplicates(nums1)
    print("测试1: nums=[1, 1, 2]")
    print(f"  返回长度: {k1}, 修改后数组前{k1}项: {nums1[:k1]}")
    print("  预期: 长度=2, 前两项=[1, 2]\n")

    # 测试用例2: 示例用例
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    print("测试2: nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]")
    print(f"  返回长度: {k2}, 修改后数组前{k2}项: {nums2[:k2]}")
    print("  预期: 长度=5, 前五项=[0, 1, 2, 3, 4]\n")

    # 测试用例3: 空数组
    nums3 = []
    k3 = sol.removeDuplicates(nums3)
    print("测试3: nums=[]")
    print(f"  返回长度: {k3}")
    print("  预期: 长度=0\n")

    # 测试用例4: 单元素
    nums4 = [1]
    k4 = sol.removeDuplicates(nums4)
    print("测试4: nums=[1]")
    print(f"  返回长度: {k4}, 修改后数组前{k4}项: {nums4[:k4]}")
    print("  预期: 长度=1, 前一项=[1]\n")

    # 测试用例5: 无重复元素
    nums5 = [1, 2, 3]
    k5 = sol.removeDuplicates(nums5)
    print("测试5: nums=[1, 2, 3]")
    print(f"  返回长度: {k5}, 修改后数组前{k5}项: {nums5[:k5]}")
    print("  预期: 长度=3, 前三项=[1, 2, 3]\n")
