class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(root:Optional[TreeNode]):
            nonlocal res
            if root:
                print(root.val)
                res.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        return res





node2 = TreeNode(3)
node3 = TreeNode(9)
node4 = TreeNode(20)
node5 = TreeNode(15)
node6 = TreeNode(7)
node1 = TreeNode(3)
node1 = TreeNode(3)

