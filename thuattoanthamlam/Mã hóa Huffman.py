import heapq
from collections import defaultdict, Counter


class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, other):
        return self.freq < other.freq


def print_huffman_code(node, val=''):
    new_val = val + str(node.huff)

    if node.left:
        print_huffman_code(node.left, new_val)
    if node.right:
        print_huffman_code(node.right, new_val)

    if not node.left and not node.right:
        print(f"{node.symbol}: {new_val}")


def huffman_encoding(data):
    frequency = Counter(data)
    nodes = [Node(freq, symbol) for symbol, freq in frequency.items()]

    heapq.heapify(nodes)

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newNode)

    print_huffman_code(nodes[0])


# Example usage:
data = "Huffman coding is a data compression algorithm."
huffman_encoding(data)
