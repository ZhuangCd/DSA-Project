import sys
from DictBinTree import DictBinTree, BinNode

tree = DictBinTree()

for line in sys.stdin:
    tree.insert(BinNode(int(line)))

print(tree.orderedTraversal())  

# run with : Get-Content input.txt | python Treesort.py > output.txt



