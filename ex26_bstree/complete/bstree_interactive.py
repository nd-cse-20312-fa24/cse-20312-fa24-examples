#!/usr/bin/env python3

from bstree import Node, BSTree
import ast

def print_help():
    print("Commands:")
    print("  (hel)p")
    print("  (q)uit")
    print("  (ins)ert <value>")
    print("  (rem)ove <value>")
    print("  (cle)ar")
    print("  (ino)rder")
    print("  (pre)order")
    print("  (pos)torder")
    print("  (pat)hs")
    print("  (gen)paths")
    print("  (rbf)s <list>--read from BFS list")
    print("  (wbf)s <list>--write to BFS list")
    print("  (hei)ght")
    print("  (bal)anced")
    print("  (isv)alidBst")
    print("  (inv)ert")
    print("  (pri)nt")
    print()

def main():
    bst = BSTree()
    print_help()

    while True:
        command_line = input("Enter command or (hel)p: ").strip().split()
        if not command_line:
            continue
        command = command_line[0].lower()
        
        # quit
        if command.startswith("q"):
            break
        # help
        elif command.startswith("hel"):
            print_help()
        # insert
        elif command.startswith("ins"):
            arg_string = " ".join(command_line[1:])
            arg = ast.literal_eval(arg_string)
            bst.insert(arg)
            print(f"Inserted {arg} into the BST.")
            print(bst)
            # try:
            #     # value = int(args[1])
            #     # arg_string = " ".join(command_line[1:])
            #     # arg = ast.literal_eval(arg_string)
            #     bst.insert(arg)
            #     print(f"Inserted {arg} into the BST.")
            #     print(bst)
            # except ValueError:
            #     print("Invalid value. Please enter an integer.")
        # remove
        elif command.startswith("rem"):
            arg_string = " ".join(command_line[1:])
            arg = ast.literal_eval(arg_string)
            bst.remove(arg)
            print(f"Deleted {arg} from the BST.")
            print(bst)
            # try:
            #     # value = int(args[1])
            #     bst.remove(arg)
            #     print(f"Deleted {arg} from the BST.")
            #     print(bst)
            # except ValueError:
            #     print("Invalid value. Please enter an integer.")
        # clear
        elif command.startswith("cle"):
            bst.clear()
            print("Cleared the BST.")
        # inorder
        elif command.startswith("ino"):
            print(bst.inorder())
        # paths
        elif command.startswith("pat"):
            print(bst.paths())
        # paths_generator
        elif command.startswith("gen"):
            print(list(bst.paths_generator()))
        # read_bfs
        elif command.startswith("rbf"):
           arg_string = " ".join(command_line[1:])
           arg = ast.literal_eval(arg_string)
           bst.read_bfs(arg)
           print(bst)
        # write_bfs
        elif command.startswith("wbf"):
            print(bst.write_bfs())
        # height
        elif command.startswith("hei"):
            print(bst.height())
        # is_balanced
        elif command.startswith("bal"):
            print(bst.is_balanced())
        # isv_valid_bst
        elif command.startswith("isv"):
            print(bst.is_valid_bst())
        # invert
        elif command.startswith("inv"):
            bst.invert()
            print(bst)
        # print
        elif command.startswith("pri"):
            print(bst)
        else:
            print("Invalid command")
            print_help()

if __name__ == "__main__":
    main()