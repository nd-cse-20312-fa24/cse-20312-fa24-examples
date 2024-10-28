from tree_print import pretty_tree
import sys

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BSTree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def __contains__(self, key):
        return self._search(self.root, key) is not None
    
    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)  
    
    def remove(self, key):
        self.root = self._remove(self.root, key)
    
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
    
    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def clear(self):
        self.root = None

    def height(self):
        return self._height(self.root)
    
    def _height(self, root):
        if root == None:
            return -1
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        return 1 + max(left_height, right_height)
        
    def is_balanced(self):
        return self._is_balanced(self.root)[0]
    
    def _is_balanced(self, root):
        if root is None:
            return True, -1
        left_balanced, left_height = self._is_balanced(root.left)
        right_balanced, right_height = self._is_balanced(root.right)
        balanced = (left_balanced and right_balanced) and abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)
        return balanced, height
    
    def invert(self):
        self.root = self._invert(self.root)
    
    def _invert(self, root):
        if root is None:
            return None
        root.left, root.right = self._invert(root.right), self._invert(root.left)
        return root
    
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, root):
        if not root:
            return []
        if root:
            return (
                self._inorder(root.left) + 
                [root.key] + 
                self._inorder(root.right))
    
    def inorder_generator(self):
        yield from self._inorder_generator(self.root)
    
    def _inorder_generator(self, root):
        if root:
            yield from self._inorder_generator(root.left)
            yield root.key
            yield from self._inorder_generator(root.right)

    def __iter__(self):
        return self.inorder_generator()
    
    def __next__(self):
        return next(self.inorder_generator())
    
    def __str__(self):
        return pretty_tree(self)
    
    def __eq__(self, other):
        if not isinstance(other, BSTree):
            return False
        return self._eq_nodes(self.root, other.root)
    
    def __len__(self):
        return self._len(self.root)
    
    def _len(self, root):
        if not root:
            return 0
        
        left_len = self._len(root.left)
        right_len = self._len(root.right)

        return 1 + left_len + right_len
    
    def _eq_nodes(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is not None and node2 is not None:
            return (node1.key == node2.key and 
                    self._eq_nodes(node1.left, node2.left) and 
                    self._eq_nodes(node1.right, node2.right))
        return False
    
    def write_bfs(self):
        if self.root is None:
            return []
        queue = [self.root]
        bfs = []
        while queue:
            node = queue.pop(0)
            if node is None:
                bfs.append(None)
            else:
                bfs.append(node.key)
                queue.append(node.left)
                queue.append(node.right)
        # Remove trailing None values
        while bfs and bfs[-1] is None:
            bfs.pop()
        return bfs


    def read_bfs(self, lst):
        if not lst:
            return
        self.root = Node(lst[0])
        queue = [self.root]
        i = 1
        while i < len(lst):
            current = queue.pop(0)
            if lst[i] is not None:
                current.left = Node(lst[i])
                queue.append(current.left)
            i += 1
            if i < len(lst) and lst[i] is not None:
                current.right = Node(lst[i])
                queue.append(current.right)
            i += 1
    
    def from_list(self, lst):
        self.root = self._from_list(lst)
    
    def _from_list(self, lst):
        if not lst:
            return None
        
        if len(lst) == 1:
            return Node(lst[0])
        if len(lst) == 2:
            return Node(lst[0], self._from_list(lst[1]))
        if len(lst) == 3:
            return Node(lst[0], self._from_list(lst[1]), self._from_list(lst[2]))

    def is_valid_bst(self):
        return self._is_valid_bst(self.root)[0]
    
    def _is_valid_bst(self, root):
        if root is None:
            return True, None, None
        
        valid_left, min_left, max_left = self._is_valid_bst(root.left)
        valid_right, min_right, max_right = self._is_valid_bst(root.right)

        if (not valid_left) or (max_left and max_left >= root.key):
            return False, None, None
        if (not valid_right) or (min_right and min_right <= root.key):
            return False, None, None

        current_min = root.key if min_left is None else min(min_left, root.key)
        current_max = root.key if max_right is None else max(max_right, root.key)

        return True, current_min, current_max
    
    # def _is_valid_bst(self, root):
    #     if root is None:
    #         return True, sys.maxsize, -sys.maxsize
        
    #     valid_left, min_left, max_left = self._is_valid_bst(root.left)
    #     valid_right, min_right, max_right = self._is_valid_bst(root.right)

    #     if (max_left >= root.key) or (min_right <= root.key):
    #         return False, 0, 0

    #     current_min = min(min_left, root.key)
    #     current_max = max(max_right, root.key)

    #     return True, current_min, current_max

    def path_to(self, key):
        return self._path_to(self.root, key)

    def _path_to(self, root, key):
        if root is None:
            return []
        if root.key == key:
            return [key]
        if key < root.key:
            return [root.key] + self._path_to(root.left, key)
        return [root.key] + self._path_to(root.right, key)
    
    def paths(self):
        return self._paths(self.root)
    
    # def _paths(self, root):
    #     if root is None:
    #         return []
        
    #     if root.left is None and root.right is None:
    #         return [[root.key]]
        
    #     all_paths = []
        
    #     if root.left:
    #         left_paths = self._paths(root.left)
    #         for path in left_paths:
    #             all_paths.append([root.key] + path)

    #     if root.right: 
    #         right_paths = self._paths(root.right)
    #         for path in right_paths:
    #             all_paths.append([root.key] + path)
                
    #     return all_paths

    # def _paths(self, root):
    #     if root is None:
    #         return []
        
    #     if root.left is None and root.right is None:
    #         return [[root.key]]
        
    #     all_paths = []
        
    #     if root.left:
    #         for path in self._paths(root.left):
    #             all_paths.append([root.key] + path)

    #     if root.right: 
    #         for path in self._paths(root.right):
    #             all_paths.append([root.key] + path)
                
    #     return all_paths
    
    # def _paths(self, root):
    #     if root is None:
    #         return []
    #     if root.left is None and root.right is None:
    #         return [[root.key]]
        
    #     left_paths = self._paths(root.left) 
    #     right_paths = self._paths(root.right)
        
    #     all_paths = [[root.key] + path for path in left_paths + right_paths]
        
    #     return all_paths

    # def _paths(self, root, path=[]):
    #     if root is None:
    #         return []
    #     if root.left is None and root.right is None:
    #         return [path + [root.key]]
        
    #     if root.left:
    #         left_paths = self._paths(root.left, path + [root.key])
    #     else:
    #         left_paths = []
    #     if root.right:
    #         right_paths = self._paths(root.right, path + [root.key])
    #     else:
    #         right_paths = []

    #     return left_paths + right_paths

    def _paths(self, root, path=[]):
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [path + [root.key]]
        
        left_paths = self._paths(root.left, path + [root.key])
        right_paths = self._paths(root.right, path + [root.key])

        return left_paths + right_paths

    # def _paths(self, root, path=[]):
    #     all_paths = []

    #     if root.left is None and root.right is None:
    #         all_paths += [path + [root.key]] 

    #     if root.left: 
    #         all_paths += self._paths(root.left, path + [root.key])
    #     if root.right:
    #         all_paths += self._paths(root.right, path + [root.key])

    #     return all_paths
    
    def paths_generator(self):
        return [path for path in self._paths_generator(self.root)]
    
    def _paths_generator(self, root, path=[]):
        if not root.left and not root.right:
            yield path + [root.key]

        if (root.left):
            yield from self._paths_generator(root.left, path + [root.key])
        if (root.right):
            yield from self._paths_generator(root.right, path + [root.key])

    
            


