#!/usr/bin/env python3

from bstree import Node, BSTree

def main():
    t1 = BSTree(Node(20, Node(10), Node(30)))
    t2 = BSTree(Node(20, Node(10), Node(31)))
    print(t1 == t2)
    print(t1.height())

if __name__ == "__main__":
    main()