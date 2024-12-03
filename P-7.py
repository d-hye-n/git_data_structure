# 코드 9.1: 이진탐색트리를 위한 노드 클래스
class BSTNode:
    def __init__ (self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None


# 코드 5.1: 배열로 구현된 원형 큐 클래스
class CircularQueue :
    def __init__( self, capacity = 8 ) :
        self.capacity = capacity        # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0                  # 전단의 인덱스
        self.rear = 0                   # 후단의 인덱스

    def isEmpty( self ) :
       return self.front == self.rear

    def isFull( self ) :
       return self.front == (self.rear+1)%self.capacity

    def enqueue( self, item ):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item

    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]


# 코드 8.6: 이진트리의 노드 수 계산
def count_node(n) :
    if n is None :
        return 0
    else :
        return 1 + count_node(n.left) + count_node(n.right)

# 코드 8.7: 이진트리의 단말노드 수 계산
def count_leaf(n) :
    if n is None : return 0
    elif n.isLeaf() : return 1
    else : return count_leaf(n.left) + count_leaf(n.right)


# 코드 8.8: 이진트리의 트리의 높이 계산
def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if hLeft > hRight : return hLeft + 1
    else: return hRight + 1

# 코드 9.13: 노드의 균형인수 계산 함수
def calc_height_diff(n) :
    if n is None:
       return 0
    return calc_height(n.left) - calc_height(n.right)

# 코드 9.14: AVL 트리의 LL회전
def rotateLL(A) :
    B = A.left
    A.left = B.right
    B.right = A
    return B

# 코드 9.15: AVL 트리의 RR회전
def rotateRR(A) :
    B = A.right
    A.right = B.left
    B.left = A
    return B

# 코드 9.16: AVL 트리의 RL회전
def rotateRL(A) :
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

# 코드 9.17: AVL 트리의 LR회전
def rotateLR(A) :
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

# 코드 9.18: AVL 트리의 재균형 함수
def reBalance (parent) :
    hDiff = calc_height_diff(parent)

    if hDiff > 1 :
        if calc_height_diff( parent.left ) > 0 :
            parent = rotateLL( parent )
        else :
            parent = rotateLR( parent )
    elif hDiff < -1 :
        if calc_height_diff( parent.right ) < 0 :
            parent = rotateRR( parent )
        else :
            parent = rotateRL( parent )
    return parent

# 코드 9.19: AVL 트리의 삽입 연산
def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left is not None:
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right is not None:
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent)
    else :
        print("중복된 키 에러")


def delete_avl(parent, key) :
    if parent is None: return None
    elif key < parent.key :
        parent.left = delete_avl(parent.left, key)
        return reBalance(parent)
    elif key > parent.key :
        parent.right = delete_avl(parent.right, key)
        return reBalance(parent)
    else :
        if parent.left is None:
            temp = parent.right
            return temp
        elif parent.right is None:
            temp = parent.left
            return temp


def levelorder(root) :
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)


# 코드 9.20: AVL 트리 테스트 프로그램
if __name__ == "__main__":
    node = [7,8,9,2,1,5,3,6,4]
    # node = [0,1,2,3,4,5,6,7,8,9]
    # node = [7]

    root = None
    for i in node :
        n = BSTNode(i)
        if root is None:
            root = n
        else :
           root = insert_avl(root, n)

        print("AVL(%d): "%i, end='')
        levelorder(root)
        print()

    print(" 노드의 개수 =", count_node(root))
    print(" 단말의 개수 =", count_leaf(root))
    print(" 트리의 높이 =", calc_height(root))

    for _ in range(int(input("삭제하고 싶은 노드 갯수를 입력하세요:"))):
        k = int(input("삭제하고 싶은 노드번호를 입력하세요:"))
        print(f"node {k} 삭제")
        delete_avl(root, k)

        print(f"AVL({k}): ", end='')
        levelorder(root)
        print()
        print(" 노드의 개수 =", count_node(root))
        print(" 단말의 개수 =", count_leaf(root))
        print(" 트리의 높이 =", calc_height(root))
