from TreePrint import pretty_tree

class Node:
    def __init__(self, key, left=None, right=None):
        pass

class Bst:
    def __init__(self, root=None):
        pass
    
    def _insert(self, root, key):
        pass
    
    def insert(self, key):
        pass

    def _search(self, root, key):
        pass
    
    def search(self, key):
        return self._search(self.root, key)
    
    def __contains__(self, key):
        pass
    
    def _inorder(self, root):
        pass
    
    def inorder(self):
        pass
    
    def clear(self):
        pass
    
    def _min_value_node(self, root):
        pass
    
    def _remove(self, root, key):
        pass
    
    def remove(self, key):
        pass

    def _height(self, root):
        pass
        
    def height(self):
        pass
    
    def __str__(self):
        return pretty_tree(self)
    
    def __eq__(self, other):
        pass
    
    def _eq_nodes(self, node1, node2):
        pass
        