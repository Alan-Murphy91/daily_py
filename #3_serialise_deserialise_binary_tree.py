class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root is None:
        return '#'
    else:
        return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(root):
    def gen_nodes():
        v = node_iter.__next__()
        if (v) == '#':
            return None
        node = Node(v)
        node.left = gen_nodes()
        node.right = gen_nodes()
        return node
    
    node_iter = iter(root.split())
    return gen_nodes()

    
node = Node(1, Node(2,Node(3)), Node(4)) 


'''
define a node class and an instance of node in the above convention.
serialize the node using python's format method.
define a class which steps through the iteration of the serialised class and performs a
recursion-based assignment of left and right nodes
'''

