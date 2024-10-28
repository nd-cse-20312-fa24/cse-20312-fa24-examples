#!/usr/bin/env python3

from bst import Node, Bst

def print_help():
    print("Commands:")
    print("  (i)nsert <value>")
    print("  (co)ntains <value>")
    print("  (t)raverse inorder")
    print("  (cl)ear")
    print("  (r)emove <value>")
    print("  (hei)ght")
    print("  (hel)p")
    print("  (q)uit")
    print()

def main():
    bst = Bst()
    print_help()
    while True:
        command = input("Enter command or (hel)p: ").strip().lower().split()
        if command[0].startswith("q"):
            break
        elif command[0].startswith("hel"):
            print_help()
        elif command[0].startswith("i"):
            try:
                value = int(command[1])
                bst.insert(value)
                print(f"Inserted {value} into the BST.")
                print(bst)
            except ValueError:
                print("Invalid value. Please enter an integer.")
        elif command[0].startswith("r"):
            try:
                value = int(command[1])
                bst.remove(value)
                print(f"Deleted {value} from the BST.")
                print(bst)
            except ValueError:
                print("Invalid value. Please enter an integer.")
        elif command[0].startswith("co"):
            try:
                value = int(command[1])
                print(value in bst)
            except ValueError:
                print("Invalid value. Please enter an integer.")
        elif command[0].startswith("cl"):
            bst.clear()
            print("BST cleared.")
        elif command[0].startswith("t"):
            print(bst.inorder())
        elif command[0].startswith("hei"):
            print(bst.height())
        else:
            print("Invalid command")
            print_help()

if __name__ == "__main__":
    main()