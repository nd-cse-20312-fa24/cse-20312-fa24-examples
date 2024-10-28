#!/usr/bin/env python3

from bst import Node, Bst

def main():
    bst = Bst()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    print(bst)
    print(bst.inorder())
    print(bst.height())
    bst.remove(3)
    print(bst)
    print(f"5 in bst: {5 in bst}")
    print(f"3 in bst: {3 in bst}")
    print(bst.inorder())
    print(bst.height())
    bst.clear()
    print(bst)

if __name__ == "__main__":
    main()
