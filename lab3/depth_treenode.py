class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_of_depths(root: TreeNode) -> int:
    if root is None:
        return 0

    depth_sum = 0
    queue = [(root, 0)]
    while queue:
        node, depth = queue.pop(0)
        depth_sum += depth

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return depth_sum


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = sum_of_depths(root)
print(result)
