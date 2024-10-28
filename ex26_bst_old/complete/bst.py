from TreePrint import pretty_tree

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class Bst:
    def __init__(self, root=None):
        self.root = root
    
    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root
    
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)
    
    def search(self, key):
        return self._search(self.root, key)
    
    def __contains__(self, key):
        return self.search(key) is not None
    
    def _inorder(self, root):
        if not root:
            return []
        if root:
            return (
                self._inorder(root.left) + 
                [root.key] + 
                self._inorder(root.right))
    
    def inorder(self):
        return self._inorder(self.root)
    
    def clear(self):
        self.root = None
    
    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.key
    
    def _remove(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._remove(root.left, key)
        elif key > root.key:
            root.right = self._remove(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            root.key = self._min_value_node(root.right)
            root.right = self._remove(root.right, root.key)
        return root
    
    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _height(self, root):
        if root == None:
            return -1
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        return 1 + max(left_height, right_height)
        
    def height(self):
        return self._height(self.root)
    
    def __str__(self):
        return pretty_tree(self)
    
    def __eq__(self, other):
        if not isinstance(other, Bst):
            return False
        return self._eq_nodes(self.root, other.root)
    
    def _eq_nodes(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is not None and node2 is not None:
            return (node1.key == node2.key and 
                    self._eq_nodes(node1.left, node2.left) and 
                    self._eq_nodes(node1.right, node2.right))
        return False
        