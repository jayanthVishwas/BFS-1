# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = [root]
        if not root:
            return res
        while q:
            temp = []
            n = len(q)
            for i in range(n):
                top = q.pop(0)
                temp.append(top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            
            res.append(temp)
            
        return res
            