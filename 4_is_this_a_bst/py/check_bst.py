class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

    def __str__(self, depth=0):
        # this snippet adapted from http://krenzel.org/articles/printing-trees
        ret = ""

        # Print right branch
        if self.right is not None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.data)

        # Print left branch
        if self.left is not None:
            ret += self.left.__str__(depth + 1)

        return ret


def build_tree(tree_string):
    """ builds a node tree object based on the HR input scheme

    :param tree_string: string space-separated values
    :return: root Node
    """
    if isinstance(tree_string, str):
        tree_string = tree_string.split(" ")
    if len(tree_string) == 1:
        return Node(int(tree_string[0]))
    else:
        mid = int(len(tree_string) / 2)
        node = Node(int(tree_string[mid]))
        left = tree_string[:mid]
        node.left = build_tree(left)
        right = tree_string[mid + 1:]
        node.right = build_tree(right)
    return node


def wrap(node, l_roots, r_roots):
    valid = True
    # print("left method {} must be less than all of {}".format(node.data, l_roots))
    for root in l_roots:
        valid = valid and node.data < root.data
    # print("right method {} must be greater than all of {}".format(node.data, r_roots))
    for root in r_roots:
        valid = valid and node.data > root.data

    if node.left:
        valid = valid and node.data > node.left.data
        # if not valid:
        #     print("not valid l1 {} {}".format(node.data, l_roots))
        valid = valid and wrap(node.left, l_roots + [node], r_roots)
        # if not valid:
        #     print("not valid l2 {} {}".format(node.data, l_roots))

    # print("after left {}".format(valid))

    if node.right:
        valid = valid and node.data < node.right.data
        # if not valid:
        #     print("not valid r1 {} {}".format(node.data, l_roots))
        valid = valid and wrap(node.right, l_roots, r_roots + [node])
        # if not valid:
        #     print("not valid r2 {} {}".format(node.data, l_roots, r_roots))
    return valid


def check_bst(root):
    return wrap(root, [], [])

