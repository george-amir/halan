def sum(node):
    sum = 0
    while(node):
            sum += node.value
            node = node.children
    return sum

class Node:
    def __init__(self, value):
        self.value = value
        self.children = None

n1 = Node(2)
n2 = Node(3)
n3 = Node(5)
n4 = Node(10)

n1.children = n2
n2.children = n3
n3.children = n4

print(sum(n1))