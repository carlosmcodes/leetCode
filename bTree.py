class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(self, root: TreeNode) -> int:
    if not root.val: return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

def isValidBST(self, root: TreeNode) -> bool:
    return dfs(root, float('-inf'), float('inf'))

def dfs(node, lower, upper):
    if not node:
        return True
    if not lower < node.val < upper:
        return False
    return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

def isSymmetric(self, root):
    return not root or isSym(root.left, root.right)

def isSym(L,R):
    if L and R and L.val == R.val: 
        return isSym(L.left, R.right) and isSym(L.right, R.left)
    return L == R