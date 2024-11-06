from tree_print import pretty_tree

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 0

class AVLTree:
    # Constructor
    # Optionally, you can initialize the tree with a root node
    def __init__(self, root=None):
        self.root = root
    
    # Clear the tree
    def clear(self):
        self.root = None

    def _get_height(self, root):
        if not root:
            return -1
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def _rebalance(self, root, key):
        balance = self._get_balance(root)

        # Case 1 - Left Left
        if balance > 1 and key < root.left.key:
            print(f"Left Left at {root.key}")
            return self._right_rotate(root)
        # Case 2 - Right Right
        if balance < -1 and key > root.right.key:
            print(f"Right Right at {root.key}")
            return self._left_rotate(root)
        # Case 3 - Left Right
        if balance > 1 and key > root.left.key:
            print(f"Left Right at {root.key}")
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        # Case 4 - Right Left
        if balance < -1 and key < root.right.key:
            print(f"Right Left at {root.key}")
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _left_rotate(self, z):
        """
        Example:
            Given the following tree:
            z
           / \
          T1  y
             / \
            T2  T3

            After _left_rotate(z), the tree becomes:
              y
             / \
            z   T3
           / \
          T1  T2
        """
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        """
        Example:
            Given the following tree:
              z
             / \
            y  T3
           / \
          T1  T2

            After _right_rotate(z), the tree becomes:
              y
             / \
            T1  z
               / \
              T2  T3
        """
        y = z.left
        T2 = y.right

        y.right = z
        z.left = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y
    
    # Insert a Node with a given key into the tree
    def insert(self, key):
        self.root = self._insert(self.root, key)

    # Helper function for insert
    def _insert(self, root, key):
        if root is None:
            return Node(key)
        
        if key == root.key:
            return root
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        return self._rebalance(root, key)
    
    # Magic method: check if the tree contains a key
    # Support for the 'in' operator
    def __contains__(self, key):
        return self._search(self.root, key) is not None
    
    # Helper function for contains
    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)  
    
    # Inorder traversal
    def inorder(self):
        return self._inorder(self.root)

    # Helper function for inorder
    def _inorder(self, root):
        if not root:
            return []

        return (
            self._inorder(root.left) + 
            [root.key] + 
            self._inorder(root.right))
    

    # Remove a Node with a given key from the tree  
    def remove(self, key):
        self.root = self._remove(self.root, key)
    
    # Helper function for remove
    def _remove(self, root, key):
        if root is None:
            return root
        
        # Key is not yet found
        if key < root.key:
            root.left = self._remove(root.left, key)
        elif key > root.key:
            root.right = self._remove(root.right, key)

        # Key is found
        else:
            # Node with only one child or leaf node: return the non-null child
            # If the node has no children, return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.key = self._min_value_node(root.right)
            # Delete the inorder successor
            root.right = self._remove(root.right, root.key)
                
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        return self._rebalance(root, key)
    
    # Helper function to find the minimum value node in a tree
    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.key
    
    # Write the BFS traversal of the tree to a list
    def write_bfs(self):
        # If the tree is empty, return an empty list
        if self.root is None:
            return []
        
        # Push the root node to the queue
        queue = [self.root]

        # List to store the BFS traversal results
        bfs = []

        # While there are nodes to process
        while queue:
            # Pop the first node from the queue
            node = queue.pop(0)

            # If the node is None (missing children), append None to the BFS list
            if node is None:
                bfs.append(None)
            
            # If the node is not None, append its key to the results and push its children to the queue
            else:
                bfs.append(node.key)
                queue.append(node.left)
                queue.append(node.right)
        
        # Remove trailing None values
        while bfs and bfs[-1] is None:
            bfs.pop()
        
        # Return the BFS traversal list
        return bfs
    
    # Magic method: string representation of the tree
    # Support for the print() function
    def __str__(self):
        return pretty_tree(self)


    
    


    

    
            


