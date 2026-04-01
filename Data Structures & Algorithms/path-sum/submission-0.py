# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # curSum=0

        # def sum(Node):

        #     if curSum!=targetSum and Node==None:
        #         return False
        #     if Node.val+curSum!=targetSum and Node.left ==None and Node.right==None:
        #         return False
        #     if Node.val+curSum==targetSum:
        #         return True
        #     else:
        #         return sum(Node.left)
        #         return sum(Node.right)
        # return sum(root)
        def dfs(node, curSum):
            if not node:
                return False

            curSum += node.val

            if not node.left and not node.right:   # 叶子
                return curSum == targetSum

            return dfs(node.left, curSum) or dfs(node.right, curSum)

        return dfs(root, 0)