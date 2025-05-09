from functools import total_ordering


@total_ordering
class Element:

    def __init__(self, key, data):
        self.key = key  # frequency
        self.data = data  # Node object(char as integer 0-255)

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key


# like:
# leaf_node = Node(97) 97 represents 'a'
# element = Element(5, leaf_node) 5 is the frequency
