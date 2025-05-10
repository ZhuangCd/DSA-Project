from PQHeap import PriorityQueue
from Node import Node
from Element import Element
from Encode2 import build_frequency_table, build_huffman_tree, build_code_table

def print_tree(node, prefix=""):
    if node is None:
        return
    if node.left is None and node.right is None:
        char = chr(node.byte) if 32 <= node.byte <= 126 else repr(chr(node.byte))
        print(f"{prefix}─ {char} (ASCII: {node.byte})")
    else:
        print(f"{prefix}─ *")
        print_tree(node.left, prefix + "  0")
        print_tree(node.right, prefix + "  1")

if __name__ == "__main__":
    input_file = r"Project 3\itslearning_files\DolphinSunset.jpg"
    freqs = build_frequency_table(input_file)
    root = build_huffman_tree(freqs)
    print_tree(root)
