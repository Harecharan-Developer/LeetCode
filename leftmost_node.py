class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root):
        level = 0
        leftmost_element = [root.val, 0]  

        def in_order_traversal(root, level):
            nonlocal leftmost_element
            if root is None:
                return
            if level > leftmost_element[1]:  
                leftmost_element = [root.val, level]
            in_order_traversal(root.left, level + 1)
            in_order_traversal(root.right, level + 1)

        in_order_traversal(root, level)
        return leftmost_element[0]

# Driver code
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Create an instance of the Solution class
    solution = Solution()

    # Call the findBottomLeftValue method and print the result
    result = solution.findBottomLeftValue(root)
    print("The bottom left value is:", result)