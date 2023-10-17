import unittest
import depth_treenode


class TestSumOfDepths(unittest.TestCase):
    """
    class
    """
    def test_empty_tree(self):
        self.assertEqual(depth_treenode.sum_of_depths(None), 0)

    def test_single_node_tree(self):
        root = depth_treenode.TreeNode(1)
        self.assertEqual(depth_treenode.sum_of_depths(root), 0)

    def test_balanced_tree(self):
        root = depth_treenode.TreeNode(1)
        root.left = depth_treenode.TreeNode(2)
        root.right = depth_treenode.TreeNode(3)
        root.left.left = depth_treenode.TreeNode(4)
        root.left.right = depth_treenode.TreeNode(5)
        self.assertEqual(depth_treenode.sum_of_depths(root), 6)

    def test_unbalanced_tree(self):
        root = depth_treenode.TreeNode(1)
        root.left = depth_treenode.TreeNode(2)
        root.left.left = depth_treenode.TreeNode(3)
        self.assertEqual(depth_treenode.sum_of_depths(root), 3)


if __name__ == '__main__':
    unittest.main()
