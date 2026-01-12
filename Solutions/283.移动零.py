#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
from typing import List


# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast = 1
        slow = 0
        length = len(nums)
        while fast < length:
            if nums[slow] == 0:
                nums[slow] = nums[fast]
                nums[fast] = 0
            fast += 1
            if nums[slow] != 0:
                slow += 1


# @lc code=end


# ==========================================
# 调试测试代码
# ==========================================
if __name__ == "__main__":
    sol = Solution()

    # 测试用例1: 示例用例
    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    print("测试1: nums=[0, 1, 0, 3, 12]")
    print(f"  移动后: {nums1}")
    print("  预期: [1, 3, 12, 0, 0]\n")

    # 测试用例2: 示例用例
    nums2 = [0]
    sol.moveZeroes(nums2)
    print("测试2: nums=[0]")
    print(f"  移动后: {nums2}")
    print("  预期: [0]\n")

    # 测试用例3: 空数组
    nums3 = []
    sol.moveZeroes(nums3)
    print("测试3: nums=[]")
    print(f"  移动后: {nums3}")
    print("  预期: []\n")

    # 测试用例4: 无零元素
    nums4 = [1, 2, 3]
    sol.moveZeroes(nums4)
    print("测试4: nums=[1, 2, 3]")
    print(f"  移动后: {nums4}")
    print("  预期: [1, 2, 3]\n")

    # 测试用例5: 全零元素
    nums5 = [0, 0, 0]
    sol.moveZeroes(nums5)
    print("测试5: nums=[0, 0, 0]")
    print(f"  移动后: {nums5}")
    print("  预期: [0, 0, 0]\n")

    # 测试用例6: 零在末尾
    nums6 = [1, 2, 0]
    sol.moveZeroes(nums6)
    print("测试6: nums=[1, 2, 0]")
    print(f"  移动后: {nums6}")
    print("  预期: [1, 2, 0]\n")
