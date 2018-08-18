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



