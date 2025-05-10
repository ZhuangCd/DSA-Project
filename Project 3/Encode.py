from Node import Node
from Element import Element
from PQHeap import PriorityQueue
from bitIO import BitWriter


def build_frequency_table(filename):
    frequencies = [0] * 256

    with open(filename, "rb") as f:
        byte = f.read(1)
        while byte:
            frequencies[byte[0]] += 1
            byte = f.read(1)

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


def build_code_table(node, prefix="", table=None):
    if table is None:
        table = [""] * 256
    if node.left is None and node.right is None:
        table[node.byte] = prefix
    else:
        build_code_table(node.left, prefix + "0", table)
        build_code_table(node.right, prefix + "1", table)
    return table


def write_frequency_table(writer, frequencies):
    for freq in frequencies:
        writer.writeint32bits(freq)


def write_encoded_data(input_filename, writer, code_table):
    with open(input_filename, "rb") as f:
        byte = f.read(1)
        while byte:
            code = code_table[byte[0]]
            for bit_char in code:
                writer.writebit(int(bit_char))
            byte = f.read(1)


if __name__ == "__main__":
    input_file = r"Project 3\itslearning_files\DolphinSunset.jpg"
    output_file = r"Project 3\encoded.bin"

    freqs = build_frequency_table(input_file)
    root = build_huffman_tree(freqs)
    code_table = build_code_table(root)

    with open(output_file, "wb") as out:
        writer = BitWriter(out)
        write_frequency_table(writer, freqs)
        write_encoded_data(input_file, writer, code_table)
        writer.flush()

    print("🌸🌸🌸 Sucess man!🌸🌸🌸")
