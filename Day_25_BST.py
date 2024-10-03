class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_bst(node, left=float('-inf'), right=float('inf')):
    if not node:
        return True
    if not (left < node.val < right):
        return False
    return (is_bst(node.left, left, node.val) and 
            is_bst(node.right, node.val, right))

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(is_bst(root))  
