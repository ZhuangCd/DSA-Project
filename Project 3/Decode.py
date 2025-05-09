from bitIO import BitReader
from Node import Node
from Element import Element
from PQHeap import PriorityQueue


def read_frequency_table(reader):
    frequencies = [0] * 256
    for i in range(256):
        frequencies[i] = reader.readint32bits()
    return frequencies


def build_huffman_tree(frequencies):
    pq = PriorityQueue()
    for byte in range(256):
        freq = frequencies[byte]
        if freq > 0:
            pq.insert(Element(freq, Node(byte)))
    while not pq.is_empty() and len(pq.heap) > 1:
        e1 = pq.extractMin()
        e2 = pq.extractMin()
        merged = Node(-1, e1.data, e2.data)
        pq.insert(Element(e1.key + e2.key, merged))
    return pq.extractMin().data


def decode_bitstream(reader, root, output_filename, total_symbols):
    with open(output_filename, "wb") as out:
        node = root
        decoded_count = 0
        while decoded_count < total_symbols:
            bit = reader.readbit()
            if bit == 0:
                node = node.left
            else:
                node = node.right

            if node.left is None and node.right is None:
                out.write(bytes([node.byte]))
                decoded_count += 1
                node = root


if __name__ == "__main__":
    input_file = r"Project 3\encoded.bin"
    output_file = r"Project 3\decoded.jpg"

    with open(input_file, "rb") as f:
        reader = BitReader(f)
        frequencies = read_frequency_table(reader)
        total_symbols = sum(frequencies)
        root = build_huffman_tree(frequencies)
        decode_bitstream(reader, root, output_file, total_symbols)
