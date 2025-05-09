class Node:
    def __init__(self, byte, left=None, right=None):
        self.byte = byte  # the char: 0-255  if its just an inner node without char: -1
        self.left = left
        self.right = right
