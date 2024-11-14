class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None


def search_bst(n, key):
    if n is None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)


def search_value_bst(n, value):
    if n is None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    return search_value_bst(n.right, value)


def search_max_bst(n):
    while n is not None and n.right is not None:
        n = n.right
    return n


def search_min_bst(n):
    while n is not None and n.left is not None:
        n = n.left
    return n


def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False


def delete_bst_case1(parent, node, root):
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root


def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right

    if node == root:
        root = child
    else:
        if node == parent.left:
            parent.left = child
        else:
            parent.right = child
    return root


def delete_bst_case3(parent, node, root):
    succp = node
    succ = node.right
    while succ.left is not None:
        succp = succ
        succ = succ.left

    if succp.left == succ:
        succp.left = succ.right
    else:
        succp.right = succ.right

    node.key = succ.key
    node.value = succ.value
    node = succ

    return root


def delete_bst(root, key):
    if root is None:
        return None

    parent = None
    node = root
    while node is not None and node.key != key:
        parent = node
        if key < node.key:
            node = node.left
        else:
            node = node.right

    if node is None:
        return root

    if node.left is None and node.right is None:
        root = delete_bst_case1(parent, node, root)

    elif node.left is None or node.right is None:
        root = delete_bst_case2(parent, node, root)

    else:
        root = delete_bst_case3(parent, node, root)

    return root


def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)


def preorder(n):
    if n is not None:
        print(n.key, end=' ')
    preorder(n.left)
    preorder(n.right)


def postorder(n):
    if n.is_not_None():
        postorder(n.left)
        postorder(n.right)
        print(n.key, end=" ")


class BSTMap():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def findMax(self):
        return search_max_bst(self.root)

    def findMin(self):
        return search_min_bst(self.root)

    def search(self, key):
        return search_bst(self.root, key)

    def searchValue(self, key):
        return search_value_bst(self.root, key)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg='BSTMap:', order=1):
        print(msg, end=" ")
        if order == 1:
            inorder(self.root)
        if order == 2:
            preorder(self.root)
        if order == 3:
            postorder(self.root)
        print()
