#!/usr/bin/env python3

import unittest
from bstree import BSTree, Node

'''
  ____30___
 /         \
10         _50___
  \       /      \
   20    40      _70
                /
               60
'''

class BstTest(unittest.TestCase):

    sample_bst = BSTree(Node(
                30, 
                Node(
                    10, 
                    None,
                    Node(20)),
                Node(
                    50, 
                    Node(40), 
                    Node(
                        70, 
                        Node(60), 
                        None))))
    
    sample_bfs = [30, 10, 50, None, 20, 40, 70, None, None, None, None, 60]

    def test_init(self):
        bst = BSTree()
        self.assertIsNone(bst.root)

    def test_init_with_root(self):
        root = Node(10)
        bst = BSTree(root)
        self.assertEqual(bst.root, root)

    def test_eq(self):
        self.assertEqual(BstTest.sample_bst, BstTest.sample_bst)

    def test_insert(self):
        '''
          ____30___
         /         \
        10         _50___
          \       /      \
           20    40      _70
                        /
                       60
        '''
        bst = BSTree()
        bst.insert(30)
        self.assertEqual(bst.root.key, 30)
        bst.insert(10)
        self.assertEqual(bst.root.left.key, 10)
        bst.insert(50)
        self.assertEqual(bst.root.right.key, 50)
        bst.insert(20)
        self.assertEqual(bst.root.left.right.key, 20)
        bst.insert(40)
        self.assertEqual(bst.root.right.left.key, 40)
        bst.insert(70)
        self.assertEqual(bst.root.right.right.key, 70)
        bst.insert(60)
        self.assertEqual(bst.root.right.right.left.key, 60)

    def test_contains(self):
        bst = BSTree()
        bst.insert(30)
        self.assertTrue(30 in bst)
        bst.insert(10)
        self.assertTrue(10 in bst)
        bst.insert(50)
        self.assertTrue(50 in bst)
        bst.insert(20)
        self.assertTrue(20 in bst)
        bst.insert(40)
        self.assertTrue(40 in bst)
        bst.insert(70)
        self.assertTrue(70 in bst)
        bst.insert(60)
        self.assertTrue(60 in bst)
        self.assertFalse(0 in bst)
        self.assertFalse(100 in bst)
    
    def test_min_value_node(self):
        bst = BSTree()
        bst.insert(3)
        self.assertEqual(bst._min_value_node(bst.root), 3)
        bst.insert(2)
        self.assertEqual(bst._min_value_node(bst.root), 2)
        bst.insert(1)
        self.assertEqual(bst._min_value_node(bst.root), 1)

    def test_remove(self):
        bst = BSTree()
        bst.insert(2)
        bst.remove(2)
        self.assertEqual(bst.root, None)
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        bst.remove(1)
        self.assertEqual(bst.root.left, None)
        self.assertEqual(bst.root.right.key, 3)
        bst.remove(3)
        self.assertEqual(bst.root.right, None)
        bst.insert(3)
        bst.remove(2)
        self.assertEqual(bst.root.key, 3)
        bst.clear()
        bst.insert(30)
        bst.insert(10)
        bst.insert(50)
        bst.insert(40)
        bst.insert(45)
        bst.remove(30)
        self.assertEqual(bst.root.key, 40)
        self.assertEqual(bst.root.right.key, 50)
        self.assertEqual(bst.root.right.left.key, 45)

    def test_to_bfs(self):
        bst = BSTree()
        bst.insert(30)
        self.assertEqual(bst.write_bfs(), [30])
        bst.insert(50)
        self.assertEqual(bst.write_bfs(), [30, None, 50])
        bst.insert(10)
        self.assertEqual(bst.write_bfs(), [30, 10, 50])
        bst.insert(20)
        bst.insert(40)
        bst.insert(70)
        self.assertEqual(bst.write_bfs(), [30, 10, 50, None, 20, 40, 70])
        bst.insert(60)
        print(bst)
        self.assertEqual(bst.write_bfs(), [30, 10, 50, None, 20, 40, 70, None, None, None, None, 60])
    
    def test_from_bfs(self):
        bst = BSTree()
        bst.read_bfs([30, 10, 50, None, 20, 40, 70, None, None, None, None, 60])
        print(bst)
        self.assertTrue(True)

    def test_height(self):
        bst = BSTree()
        self.assertEqual(bst.height(), -1)
        bst.insert(30)
        self.assertEqual(bst.height(), 0)
        bst.insert(10)
        self.assertEqual(bst.height(), 1)
        bst.insert(50)
        self.assertEqual(bst.height(), 1)
        bst.insert(20)
        self.assertEqual(bst.height(), 2)
        bst.insert(40)
        self.assertEqual(bst.height(), 2)
        bst.insert(70)
        self.assertEqual(bst.height(), 2)
        bst.insert(60)
        self.assertEqual(bst.height(), 3)

    def test_is_balanced(self):
        bst = BSTree()
        self.assertTrue(bst.is_balanced())
        bst.insert(30)
        self.assertTrue(bst.is_balanced())
        bst.insert(10)
        self.assertTrue(bst.is_balanced())
        bst.insert(20)
        self.assertFalse(bst.is_balanced())
        bst.insert(50)
        self.assertTrue(bst.is_balanced())
        bst.insert(70)
        self.assertTrue(bst.is_balanced())
        bst.insert(60)
        self.assertFalse(bst.is_balanced())
        bst.insert(40)
        self.assertTrue(bst.is_balanced())

    def test_invert(self):
        bst = BSTree()
        bst.insert(30)
        bst.invert()
        self.assertEqual(bst.root.key, 30)
        bst.invert()
        bst.insert(10)
        bst.invert()
        self.assertEqual(bst.root.right.key, 10)
        bst.invert()
        bst.insert(50)
        bst.invert()
        self.assertEqual(bst.root.left.key, 50)
        self.assertEqual(bst.root.right.key, 10)
        bst.invert()
        bst.insert(20)
        bst.insert(40)
        bst.insert(70)
        bst.insert(60)
        bst.invert()
        self.assertEqual(bst.root.key, 30)
        self.assertEqual(bst.root.left.key, 50)
        self.assertEqual(bst.root.right.key, 10)
        self.assertEqual(bst.root.left.left.key, 70)
        self.assertEqual(bst.root.left.right.key, 40)
        self.assertEqual(bst.root.right.left.key, 20)
        self.assertEqual(bst.root.left.left.right.key, 60)

    def test_from_list(self):
        bst = BSTree()
        bst.from_list([2])
        self.assertEqual(bst.root.key, 2)
        bst.from_list([2, [1]])
        self.assertEqual(bst.root.key, 2)
        self.assertEqual(bst.root.left.key, 1)
        bst.from_list([2, [1], [3]])
        self.assertEqual(bst.root.key, 2)
        self.assertEqual(bst.root.left.key, 1)
        self.assertEqual(bst.root.right.key, 3)
        bst.from_list([30, [10, None, [20]], [50, [40], [70, [60]]]])
        self.assertEqual(bst.root.key, 30)
        self.assertEqual(bst.root.left.key, 10)
        self.assertEqual(bst.root.left.right.key, 20)
        self.assertEqual(bst.root.right.key, 50)
        self.assertEqual(bst.root.right.left.key, 40)
        self.assertEqual(bst.root.right.right.key, 70)
        self.assertEqual(bst.root.right.right.left.key, 60)

    def test_is_valid_bst(self):
        bst = BSTree()
        bst.read_bfs([40])
        self.assertTrue(bst.is_valid_bst())
        bst.read_bfs([40, 20, 60])
        self.assertTrue(bst.is_valid_bst())
        bst.read_bfs([40, 60])
        self.assertFalse(bst.is_valid_bst())
        bst.read_bfs([40, None, 20])
        self.assertFalse(bst.is_valid_bst())
        bst.read_bfs([40, 20, 60, 10, 30, 50, 70])
        self.assertTrue(bst.is_valid_bst())
        bst.read_bfs([40, 20, 60, 10, 80, 50, 70])
        self.assertFalse(bst.is_valid_bst())
        bst.read_bfs([40, 20, 60, 10, 30, 5, 70])
        self.assertFalse(bst.is_valid_bst())

    def test_len(self):
        bst = BSTree()
        self.assertEqual(len(bst), 0)
        bst.insert(30)
        self.assertEqual(len(bst), 1)
        bst.insert(10)
        self.assertEqual(len(bst), 2)
        bst.insert(50)
        self.assertEqual(len(bst), 3)
        bst.insert(20)
        self.assertEqual(len(bst), 4)
        bst.insert(40)
        self.assertEqual(len(bst), 5)
        bst.insert(70)
        self.assertEqual(len(bst), 6)
        bst.insert(60)
        self.assertEqual(len(bst), 7)

