class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Insert a value into the binary tree
    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Traversals
    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

    def preorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        return result

    def postorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
        return result

    def level_order_traversal(self):
        if not self.root:
            return []
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    # Search for a value in the tree
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    # Delete a value from the tree
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
        return node

    # Find the minimum value in the tree
    def find_min(self):
        return self._find_min_recursive(self.root)

    def _find_min_recursive(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.value

    # Find the maximum value in the tree
    def find_max(self):
        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.value

    # Height of the tree
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    # Diameter of the tree (longest path between any two nodes)
    def diameter(self):
        return self._diameter_recursive(self.root)[0]

    def _diameter_recursive(self, node):
        if node is None:
            return (0, 0)  # (diameter, height)
        left_diameter, left_height = self._diameter_recursive(node.left)
        right_diameter, right_height = self._diameter_recursive(node.right)
        current_height = max(left_height, right_height) + 1
        current_diameter = max(left_diameter, right_diameter, left_height + right_height + 1)
        return (current_diameter, current_height)

    # Check if the tree is balanced
    def is_balanced(self):
        return self._is_balanced_recursive(self.root)

    def _is_balanced_recursive(self, node):
        if node is None:
            return True
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        if abs(left_height - right_height) <= 1 and self._is_balanced_recursive(node.left) and self._is_balanced_recursive(node.right):
            return True
        return False

    # Check if the tree is a valid Binary Search Tree (BST)
    def is_bst(self):
        return self._is_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_bst_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        if node.value <= min_val or node.value >= max_val:
            return False
        return self._is_bst_recursive(node.left, min_val, node.value) and self._is_bst_recursive(node.right, node.value, max_val)

    # Find the Lowest Common Ancestor (LCA) of two nodes
    def lca(self, p, q):
        return self._lca_recursive(self.root, p, q)

    def _lca_recursive(self, node, p, q):
        if node is None:
            return None
        if node.value == p or node.value == q:
            return node
        left = self._lca_recursive(node.left, p, q)
        right = self._lca_recursive(node.right, p, q)
        if left and right:
            return node
        return left if left else right

    # Count the number of nodes in the tree
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    # Count the number of leaf nodes in the tree
    def count_leaf_nodes(self):
        return self._count_leaf_nodes_recursive(self.root)

    def _count_leaf_nodes_recursive(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaf_nodes_recursive(node.left) + self._count_leaf_nodes_recursive(node.right)

    # Print all leaf nodes
    def print_leaf_nodes(self):
        self._print_leaf_nodes_recursive(self.root)

    def _print_leaf_nodes_recursive(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.value, end=" ")
        self._print_leaf_nodes_recursive(node.left)
        self._print_leaf_nodes_recursive(node.right)

    # Check if the tree is a full binary tree
    def is_full(self):
        return self._is_full_recursive(self.root)

    def _is_full_recursive(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self._is_full_recursive(node.left) and self._is_full_recursive(node.right)
        return False

    # Check if the tree is a complete binary tree
    def is_complete(self):
        total_nodes = self.count_nodes()
        return self._is_complete_recursive(self.root, 0, total_nodes)

    def _is_complete_recursive(self, node, index, total_nodes):
        if node is None:
            return True
        if index >= total_nodes:
            return False
        return (self._is_complete_recursive(node.left, 2 * index + 1, total_nodes) and
                self._is_complete_recursive(node.right, 2 * index + 2, total_nodes))

    # Mirror the tree
    def mirror(self):
        self._mirror_recursive(self.root)

    def _mirror_recursive(self, node):
        if node is None:
            return
        self._mirror_recursive(node.left)
        self._mirror_recursive(node.right)
        node.left, node.right = node.right, node.left

class BinarySearchTree(BinaryTree):
    # Insert a value into the BST
    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    # Delete a value from the BST
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
        return node

    # Find the minimum value in the BST
    def find_min(self):
        return self._find_min_recursive(self.root)

    def _find_min_recursive(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.value

    # Find the maximum value in the BST
    def find_max(self):
        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.value


    # Height of the tree
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    # Diameter of the tree (longest path between any two nodes)
    def diameter(self):
        return self._diameter_recursive(self.root)[0]

    def _diameter_recursive(self, node):
        if node is None:
            return (0, 0)  # (diameter, height)
        left_diameter, left_height = self._diameter_recursive(node.left)
        right_diameter, right_height = self._diameter_recursive(node.right)
        current_height = max(left_height, right_height) + 1
        current_diameter = max(left_diameter, right_diameter, left_height + right_height + 1)
        return (current_diameter, current_height)

    # Check if the tree is balanced
    def is_balanced(self):
        return self._is_balanced_recursive(self.root)

    def _is_balanced_recursive(self, node):
        if node is None:
            return True
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        if abs(left_height - right_height) <= 1 and self._is_balanced_recursive(node.left) and self._is_balanced_recursive(node.right):
            return True
        return False

    # Check if the tree is a valid Binary Search Tree (BST)
    def is_bst(self):
        return self._is_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_bst_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        if node.value <= min_val or node.value >= max_val:
            return False
        return self._is_bst_recursive(node.left, min_val, node.value) and self._is_bst_recursive(node.right, node.value, max_val)

    # Find the Lowest Common Ancestor (LCA) of two nodes
    def lca(self, p, q):
        return self._lca_recursive(self.root, p, q)

    def _lca_recursive(self, node, p, q):
        if node is None:
            return None
        if node.value == p or node.value == q:
            return node
        left = self._lca_recursive(node.left, p, q)
        right = self._lca_recursive(node.right, p, q)
        if left and right:
            return node
        return left if left else right

    # Count the number of nodes in the tree
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    # Count the number of leaf nodes in the tree
    def count_leaf_nodes(self):
        return self._count_leaf_nodes_recursive(self.root)

    def _count_leaf_nodes_recursive(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaf_nodes_recursive(node.left) + self._count_leaf_nodes_recursive(node.right)

    # Print all leaf nodes
    def print_leaf_nodes(self):
        self._print_leaf_nodes_recursive(self.root)

    def _print_leaf_nodes_recursive(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.value, end=" ")
        self._print_leaf_nodes_recursive(node.left)
        self._print_leaf_nodes_recursive(node.right)

    # Check if the tree is a full binary tree
    def is_full(self):
        return self._is_full_recursive(self.root)

    def _is_full_recursive(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self._is_full_recursive(node.left) and self._is_full_recursive(node.right)
        return False

    # Check if the tree is a complete binary tree
    def is_complete(self):
        total_nodes = self.count_nodes()
        return self._is_complete_recursive(self.root, 0, total_nodes)

    def _is_complete_recursive(self, node, index, total_nodes):
        if node is None:
            return True
        if index >= total_nodes:
            return False
        return (self._is_complete_recursive(node.left, 2 * index + 1, total_nodes) and
                self._is_complete_recursive(node.right, 2 * index + 2, total_nodes))

    # Mirror the tree
    def mirror(self):
        self._mirror_recursive(self.root)

    def _mirror_recursive(self, node):
        if node is None:
            return
        self._mirror_recursive(node.left)
        self._mirror_recursive(node.right)
        node.left, node.right = node.right, node.left


def printStructure():
  return """
  bt = BinaryTree()
  bt.insert(10)
  bt.insert(5)
  bt.insert(15)
  bt.insert(2)
  bt.insert(7)
  
  # Traversals
  print("Inorder Traversal:", bt.inorder_traversal(bt.root))
  print("Preorder Traversal:", bt.preorder_traversal(bt.root))
  print("Postorder Traversal:", bt.postorder_traversal(bt.root))
  print("Level Order Traversal:", bt.level_order_traversal())
  
  # Tree Properties
  print("Height of the Tree:", bt.height())
  print("Diameter of the Tree:", bt.diameter())
  print("Is Balanced:", bt.is_balanced())
  print("Is BST:", bt.is_bst())
  
  # Node Operations
  print("Min Value in Tree:", bt.find_min())
  print("Max Value in Tree:", bt.find_max())
  print("Number of Nodes:", bt.count_nodes())
  print("Number of Leaf Nodes:", bt.count_leaf_nodes())
  print("Leaf Nodes:", end=" ")
  bt.print_leaf_nodes()
  
  # Tree Checks
  print("\nIs Full Binary Tree:", bt.is_full())
  print("Is Complete Binary Tree:", bt.is_complete())
  
  # Advanced Operations
  print("LCA of 2 and 7:", bt.lca(2, 7).value)
  bt.mirror()
  print("Inorder Traversal after Mirroring:", bt.inorder_traversal(bt.root))
  
  
  
  bst = BinarySearchTree()
  bst.insert(10)
  bst.insert(5)
  bst.insert(15)
  bst.insert(2)
  bst.insert(7)
  
  # Traversals
  print("Inorder Traversal:", bst.inorder_traversal(bst.root))
  
  # BST-Specific Operations
  print("Search for 5:", bst.search(5) is not None)
  bst.delete(5)
  print("Inorder Traversal after deletion:", bst.inorder_traversal(bst.root))
  print("Max Value in BST:", bst.find_max())
  print("Min Value in BST:", bst.find_min())
  """

def printCode():
  return """
  class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Insert a value into the binary tree
    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Traversals
    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

    def preorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        return result

    def postorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
        return result

    def level_order_traversal(self):
        if not self.root:
            return []
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    # Search for a value in the tree
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    # Delete a value from the tree
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
        return node

    # Find the minimum value in the tree
    def find_min(self):
        return self._find_min_recursive(self.root)

    def _find_min_recursive(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.value

    # Find the maximum value in the tree
    def find_max(self):
        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.value

    # Height of the tree
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    # Diameter of the tree (longest path between any two nodes)
    def diameter(self):
        return self._diameter_recursive(self.root)[0]

    def _diameter_recursive(self, node):
        if node is None:
            return (0, 0)  # (diameter, height)
        left_diameter, left_height = self._diameter_recursive(node.left)
        right_diameter, right_height = self._diameter_recursive(node.right)
        current_height = max(left_height, right_height) + 1
        current_diameter = max(left_diameter, right_diameter, left_height + right_height + 1)
        return (current_diameter, current_height)

    # Check if the tree is balanced
    def is_balanced(self):
        return self._is_balanced_recursive(self.root)

    def _is_balanced_recursive(self, node):
        if node is None:
            return True
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        if abs(left_height - right_height) <= 1 and self._is_balanced_recursive(node.left) and self._is_balanced_recursive(node.right):
            return True
        return False

    # Check if the tree is a valid Binary Search Tree (BST)
    def is_bst(self):
        return self._is_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_bst_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        if node.value <= min_val or node.value >= max_val:
            return False
        return self._is_bst_recursive(node.left, min_val, node.value) and self._is_bst_recursive(node.right, node.value, max_val)

    # Find the Lowest Common Ancestor (LCA) of two nodes
    def lca(self, p, q):
        return self._lca_recursive(self.root, p, q)

    def _lca_recursive(self, node, p, q):
        if node is None:
            return None
        if node.value == p or node.value == q:
            return node
        left = self._lca_recursive(node.left, p, q)
        right = self._lca_recursive(node.right, p, q)
        if left and right:
            return node
        return left if left else right

    # Count the number of nodes in the tree
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    # Count the number of leaf nodes in the tree
    def count_leaf_nodes(self):
        return self._count_leaf_nodes_recursive(self.root)

    def _count_leaf_nodes_recursive(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaf_nodes_recursive(node.left) + self._count_leaf_nodes_recursive(node.right)

    # Print all leaf nodes
    def print_leaf_nodes(self):
        self._print_leaf_nodes_recursive(self.root)

    def _print_leaf_nodes_recursive(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.value, end=" ")
        self._print_leaf_nodes_recursive(node.left)
        self._print_leaf_nodes_recursive(node.right)

    # Check if the tree is a full binary tree
    def is_full(self):
        return self._is_full_recursive(self.root)

    def _is_full_recursive(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self._is_full_recursive(node.left) and self._is_full_recursive(node.right)
        return False

    # Check if the tree is a complete binary tree
    def is_complete(self):
        total_nodes = self.count_nodes()
        return self._is_complete_recursive(self.root, 0, total_nodes)

    def _is_complete_recursive(self, node, index, total_nodes):
        if node is None:
            return True
        if index >= total_nodes:
            return False
        return (self._is_complete_recursive(node.left, 2 * index + 1, total_nodes) and
                self._is_complete_recursive(node.right, 2 * index + 2, total_nodes))

    # Mirror the tree
    def mirror(self):
        self._mirror_recursive(self.root)

    def _mirror_recursive(self, node):
        if node is None:
            return
        self._mirror_recursive(node.left)
        self._mirror_recursive(node.right)
        node.left, node.right = node.right, node.left

class BinarySearchTree(BinaryTree):
    # Insert a value into the BST
    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    # Delete a value from the BST
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
        return node

    # Find the minimum value in the BST
    def find_min(self):
        return self._find_min_recursive(self.root)

    def _find_min_recursive(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.value

    # Find the maximum value in the BST
    def find_max(self):
        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.value

    # Height of the tree
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    # Diameter of the tree (longest path between any two nodes)
    def diameter(self):
        return self._diameter_recursive(self.root)[0]

    def _diameter_recursive(self, node):
        if node is None:
            return (0, 0)  # (diameter, height)
        left_diameter, left_height = self._diameter_recursive(node.left)
        right_diameter, right_height = self._diameter_recursive(node.right)
        current_height = max(left_height, right_height) + 1
        current_diameter = max(left_diameter, right_diameter, left_height + right_height + 1)
        return (current_diameter, current_height)

    # Check if the tree is balanced
    def is_balanced(self):
        return self._is_balanced_recursive(self.root)

    def _is_balanced_recursive(self, node):
        if node is None:
            return True
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        if abs(left_height - right_height) <= 1 and self._is_balanced_recursive(node.left) and self._is_balanced_recursive(node.right):
            return True
        return False

    # Check if the tree is a valid Binary Search Tree (BST)
    def is_bst(self):
        return self._is_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_bst_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        if node.value <= min_val or node.value >= max_val:
            return False
        return self._is_bst_recursive(node.left, min_val, node.value) and self._is_bst_recursive(node.right, node.value, max_val)

    # Find the Lowest Common Ancestor (LCA) of two nodes
    def lca(self, p, q):
        return self._lca_recursive(self.root, p, q)

    def _lca_recursive(self, node, p, q):
        if node is None:
            return None
        if node.value == p or node.value == q:
            return node
        left = self._lca_recursive(node.left, p, q)
        right = self._lca_recursive(node.right, p, q)
        if left and right:
            return node
        return left if left else right

    # Count the number of nodes in the tree
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    # Count the number of leaf nodes in the tree
    def count_leaf_nodes(self):
        return self._count_leaf_nodes_recursive(self.root)

    def _count_leaf_nodes_recursive(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaf_nodes_recursive(node.left) + self._count_leaf_nodes_recursive(node.right)

    # Print all leaf nodes
    def print_leaf_nodes(self):
        self._print_leaf_nodes_recursive(self.root)

    def _print_leaf_nodes_recursive(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.value, end=" ")
        self._print_leaf_nodes_recursive(node.left)
        self._print_leaf_nodes_recursive(node.right)

    # Check if the tree is a full binary tree
    def is_full(self):
        return self._is_full_recursive(self.root)

    def _is_full_recursive(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self._is_full_recursive(node.left) and self._is_full_recursive(node.right)
        return False

    # Check if the tree is a complete binary tree
    def is_complete(self):
        total_nodes = self.count_nodes()
        return self._is_complete_recursive(self.root, 0, total_nodes)

    def _is_complete_recursive(self, node, index, total_nodes):
        if node is None:
            return True
        if index >= total_nodes:
            return False
        return (self._is_complete_recursive(node.left, 2 * index + 1, total_nodes) and
                self._is_complete_recursive(node.right, 2 * index + 2, total_nodes))

    # Mirror the tree
    def mirror(self):
        self._mirror_recursive(self.root)

    def _mirror_recursive(self, node):
        if node is None:
            return
        self._mirror_recursive(node.left)
        self._mirror_recursive(node.right)
        node.left, node.right = node.right, node.left

    """
