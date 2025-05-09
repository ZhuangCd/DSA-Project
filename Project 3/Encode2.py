from PQHeap import PriorityQueue
from Node import Node
from Element import Element
from bitIO import BitWriter


def build_frequency_table(input_filename):
    frequencies = [0] * 256

    with open(input_filename, "rb") as f:
        byte = f.read(1)  # read the first byte

        while byte:
            value = byte[0]  # numeric value of the byte (0-255)
            frequencies[value] += 1
            byte = f.read(1)

        return frequencies  # [0,0,1,1,0,0...]


def build_huffman_tree(frequencies):
    pq = PriorityQueue()

    for byte in range(256):
        if frequencies[byte] > 0:
            node = Node(byte)
            e = Element(frequencies[byte], node)
            pq.insert(e)

        while not pq.is_empty() and len(pq.heap) > 1:
            e1 = pq.extractMin()
            e2 = pq.extractMin()
            new_node = Node(-1, e1.data, e2.data)
            new_element = Element(e1.key + e2.key, new_node)
            pq.insert(new_element)
        
            return pq.extractMin().data

def build_code_table(node, prefix="", table=None):
    if table is None:
        table = [""] * 256

    if node.left is None and node.right is None:
        table[node.byte] = prefix

    else: 
        build_code_table(node.left, prefix + "0", table)
        build_code_table(node.right, prefix + "1", table)

    return table # ["", 4, 10, "", ..]

# at the beginning of the file: [0, 0, ..., 0, 5, ...]
def write_frequency_table(writer, frequencies):
    for freq in frequencies:
        writer.writeint32bits(freq)  # 32 bits (4 byte) 


def write_encoded_data(input_filename, code_table, writer):
    with open(input_filename, "rb") as f:
        byte = f.read(1)
        while byte:
            code = code_table[byte[0]]
            for bit_char in code:
                writer.writebit(int(bit_char))
            byte = f.read(1)


def compress_file(input_file, output_file):
    frequencies = build_frequency_table(input_file)
    root = build_huffman_tree(frequencies)
    code_table = build_code_table(root)

    with open(output_file, "wb") as f:
        writer = BitWriter(f)
        write_frequency_table(writer, frequencies)
        write_encoded_data(input_file, code_table, writer)
        writer.flush()

if __name__ == "__main__":
    compress_file("Project 3\KingJamesBible.txt","Project 3\encoded.bin" )
    print("🏵️🏵️🏵️  Sucess man!🏵️🏵️🏵️")
