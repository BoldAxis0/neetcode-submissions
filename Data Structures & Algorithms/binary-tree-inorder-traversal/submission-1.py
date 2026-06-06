# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        #go all the way left 
        #keep exploring left until you cant
        #if no more left children, add value to list
        #once left exploration is complete, add parent to list
        #and then go right 

        #ignore nulls
        if not root:
            return []

        nums = []

        def traverse(node:Optional[TreeNode]):

            if node.left:
                traverse(node.left)

            nums.append(node.val)

            if node.right:
                traverse(node.right)
        
        traverse(root)
        
        return nums




        