import collections

# ==========================================
# 基础数据结构定义 (与 LeetCode 保持一致)
# ==========================================


class ListNode:
    """单链表节点定义"""

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    # 方便打印调试：当你 print(node) 时显示直观的链表结构
    def __repr__(self):
        return f"{self.val} -> {self.next}"


class TreeNode:
    """二叉树节点定义"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # 方便打印调试：显示当前节点值
    def __repr__(self):
        return f"TreeNode({self.val})"


# ==========================================
# 核心辅助函数 (用于本地构建测试用例)
# ==========================================


def list_to_linkedlist(nums):
    """
    将 Python 列表转换为链表
    输入: [1, 2, 3]
    输出: ListNode(1) -> ListNode(2) -> ListNode(3)
    """
    dummy = ListNode(0)
    ptr = dummy
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
    return dummy.next


def linkedlist_to_list(head):
    """
    将链表转换回 Python 列表 (方便验证结果)
    """
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def list_to_binarytree(nums):
    """
    将 Python 列表转换为二叉树 (层序遍历构建，适配 LeetCode 输入格式)
    输入: [3, 9, 20, None, None, 15, 7]
    输出: TreeNode 对象
    """
    if not nums:
        return None

    # LeetCode 的输入通常把 null 表示为 None
    iter_nums = iter(nums)
    root = TreeNode(next(iter_nums))
    q = collections.deque([root])

    while q:
        node = q.popleft()

        # 处理左子节点
        try:
            val = next(iter_nums)
            if val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
        except StopIteration:
            break

        # 处理右子节点
        try:
            val = next(iter_nums)
            if val is not None:
                node.right = TreeNode(val)
                q.append(node.right)
        except StopIteration:
            break

    return root
